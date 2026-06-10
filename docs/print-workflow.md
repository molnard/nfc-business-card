# Print Workflow

## Current Model

Use this Bambu Studio project file:

```text
bambu/davidmolnar-dev-business-card-public.3mf
```

Older prototype STL/SVG/3MF files are not part of the current workflow.

## NFC Programming

Write this exact URL to the physical NFC tag:

```text
https://davidmolnar.dev/addcontact
```

Do not write old endpoints such as `/c`, `/contact`, or `/contact.vcf`.

Suggested NFC Tools PRO flow:

1. Open NFC Tools PRO.
2. Go to `Write`.
3. Clear any old record list.
4. Add one `URL / URI` record.
5. Enter `https://davidmolnar.dev/addcontact`.
6. Tap `Write`.
7. Hold the phone to the NFC tag until writing succeeds.

## Printing Notes

- Open the current 3MF in Bambu Studio.
- The current card is NFC-first and does not include a printed QR code.
- Use the existing pause workflow in the project file to insert the NFC sticker.
- Place the sticker carefully in the recessed area before resuming the print.
- Avoid metallic foil, magnetic material, carbon-filled filament, or metal backing near the NFC antenna.
- Test the tag before and after the print.

## Optional QR Fallback

QR assets exist for possible future use, but they are not part of the current printed card.

Small QR codes are difficult to print cleanly on this surface. If QR fallback becomes necessary later, prefer a tested sticker or another reliable non-FDM method before treating it as production-ready.

## Validation

After printing:

1. Scan the NFC tag with Android.
2. Scan the NFC tag with iPhone.
3. Confirm both open `https://davidmolnar.dev/addcontact`.
4. Confirm the add/save contact button works on the page.
