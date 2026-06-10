# NFC Business Card

![Printed NFC business card preview](assets/preview.jpg)

Customized 3D printed NFC business card for Dávid Molnár.

The current printed card does not include a QR code. QR assets are kept only as a future fallback option because small printed QR codes are difficult to print reliably and no QR sticker has been prepared yet.

The production NFC tag should be programmed with this exact URL:

```text
https://davidmolnar.dev/addcontact
```

`/addcontact` opens the mobile contact page with the add/save contact button. Do not program older test endpoints such as `/c`, `/contact`, or `/contact.vcf` onto new physical NFC tags.

## Current Files

- `bambu/davidmolnar-dev-business-card-public.3mf` - current Bambu Studio project file
- `assets/preview.jpg` - public product preview image
- `assets/qr-addcontact.svg` - optional future QR fallback for the production contact URL
- `assets/qr-addcontact.png` - optional phone-testable QR image for the production contact URL
- `docs/design-decisions.md` - NFC/contact-flow decisions from the project conversations
- `docs/print-workflow.md` - Bambu Studio and NFC programming workflow
- `tools/generate_qr_assets.py` - regenerates optional `/addcontact` QR assets

## Optional QR Assets

```bash
python tools/generate_qr_assets.py
```

These QR files are not part of the current printed card. They are kept for a possible later sticker, insert, or alternate card revision.

## Print Notes

Open `bambu/davidmolnar-dev-business-card-public.3mf` in Bambu Studio. The original profile was designed for a 0.2 mm NFC tag sticker workflow with a pause for inserting the tag.

Use `docs/print-workflow.md` for the current print and NFC programming checklist.

## Attribution

This card is a customized derivative of:

- Original design: `Fancy Tech NFC Business Card - Fully Customizable`
- Designer: `EricP`
- Source: https://makerworld.com/hu/models/2335591-fancy-tech-nfc-business-card-fully-customizable#profileId-2554972

## License

This repository uses split licensing:

- 3D design assets and previews derived from the MakerWorld model are under CC BY-SA 4.0.
- Utility scripts in `tools/` are under MIT.

See `LICENSE.md` for details.
