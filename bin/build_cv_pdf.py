"""Build assets/rendercv/rendercv_output/Yoonjae_Baek_CV.pdf from _data/cv.yml.

RenderCV lays out the page from assets/rendercv/design.yaml. Publications are typeset here as a
numbered list with a hanging indent, which RenderCV's templates cannot express: the section is
rendered as a placeholder, swapped for Typst markup, and the result compiled with RenderCV's fonts.

Setup:  uv tool install "rendercv[full]"
Run:    ~/.local/share/uv/tools/rendercv/bin/python bin/build_cv_pdf.py
"""
import pathlib, re, subprocess, sys, tempfile

from ruamel.yaml import YAML
from rendercv.renderer.pdf_png import get_typst_compiler

repo = pathlib.Path(__file__).resolve().parent.parent
out_pdf = repo / "assets/rendercv/rendercv_output/Yoonjae_Baek_CV.pdf"
PLACEHOLDER = "RCVPUBLICATIONSPLACEHOLDER"

yaml = YAML(typ="safe")
data = yaml.load((repo / "_data/cv.yml").read_text())
cv = data["cv"]
# Fields the al-folio web CV reads but RenderCV rejects, plus header items the PDF leaves out.
for key in ("label", "image", "summary", "address", "location", "social_networks"):
    cv.pop(key, None)
sections = cv["sections"]
# The section title already says "Interests", so the PDF keeps only the keywords.
sections["Interests"] = [e["keywords"] for e in sections.get("Interests", [])]
publications = sections["Publications"]
# Honors and services read as one full-width line ("**Name**, detail, year"), with any summary below.
for title in ("Honors and Awards", "Services"):
    sections[title] = [
        f"**{e['name']}**, {e['detail']}, {str(e['date'])[:4]}"
        + (f"#linebreak(){e['summary']}" if e.get("summary") else "")
        for e in sections.get(title, [])
    ]
sections["Publications"] = [PLACEHOLDER]


def esc(text):
    return re.sub(r"([\\*_#$@<>\[\]`~])", r"\\\1", text)


def author(name):
    # "**Name**\*" -> bold name; keep each name on one line.
    m = re.fullmatch(r"\*\*(.+?)\*\*(.*)", name)
    core, tail = (m.group(1), m.group(2)) if m else (name, "")
    core = esc(core.replace("\\*", "*")).replace(" ", " ").replace("-", "-⁠")
    tail = esc(tail.replace("\\*", "*"))
    return (f"#strong[{core}]" if m else core) + tail


items = []
for p in publications:
    authors = ", ".join(author(a) for a in p["authors"])
    note = p.get("summary", "").replace("\\*", "*")
    if note:
        authors += f" ({esc(note)})"
    items.append(f"+ #strong[#emph[{esc(p['title'])}]] \\\n  {authors} \\\n  {esc(p['journal'])}, {p['date']}")
# A content block keeps the enum styling from leaking into (and regrouping) the later sections.
pub_typst = (
    '#[\n#set enum(numbering: "[1]", number-align: end + top, body-indent: 0.6em, spacing: 0.85em)\n'
    + "\n".join(items)
    + "\n]"
)

with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    YAML().dump(data, tmp / "cv.yml")
    rendercv = pathlib.Path(sys.executable).with_name("rendercv")
    subprocess.run(
        [str(rendercv), "render", str(tmp / "cv.yml"), "--design", str(repo / "assets/rendercv/design.yaml"),
         "--typst-path", str(tmp / "cv.typ"), "--dont-generate-pdf", "--dont-generate-markdown",
         "--dont-generate-html", "--dont-generate-png"],
        check=True, capture_output=True,
    )
    typ = (tmp / "cv.typ").read_text()
    assert typ.count(PLACEHOLDER) == 1, "publications placeholder not found in generated Typst"
    typ = "\n".join(pub_typst if PLACEHOLDER in line else line for line in typ.splitlines())
    (tmp / "cv.typ").write_text(typ)
    get_typst_compiler(tmp / "cv.yml", tmp).compile(input=tmp / "cv.typ", format="pdf", output=out_pdf)
print(out_pdf)
