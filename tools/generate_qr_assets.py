from __future__ import annotations

from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M


URL = "https://davidmolnar.dev/addcontact"
OUT = Path("assets")


def write_svg(matrix: list[list[bool]], path: Path, module_mm: float = 0.8, quiet: int = 4) -> None:
    size = len(matrix)
    total = (size + quiet * 2) * module_mm
    rects = []

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell:
                rects.append(
                    f'<rect x="{(x + quiet) * module_mm:.2f}" y="{(y + quiet) * module_mm:.2f}" '
                    f'width="{module_mm:.2f}" height="{module_mm:.2f}"/>'
                )

    path.write_text(
        "\n".join(
            [
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{total:.2f}mm" height="{total:.2f}mm" viewBox="0 0 {total:.2f} {total:.2f}">',
                '<rect width="100%" height="100%" fill="#ffffff"/>',
                '<g fill="#111111">',
                *rects,
                "</g>",
                "</svg>",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=32,
        border=4,
    )
    qr.add_data(URL)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    image.save(OUT / "qr-addcontact.png", dpi=(600, 600))

    large = image.resize((1200, 1200), resample=0)
    large.save(OUT / "qr-addcontact-1200.png", dpi=(600, 600))

    write_svg(qr.get_matrix(), OUT / "qr-addcontact.svg")


if __name__ == "__main__":
    main()
