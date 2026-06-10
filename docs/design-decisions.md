# Design Decisions

## Final NFC Target

Program the physical NFC tag with:

```text
https://davidmolnar.dev/addcontact
```

This is the final production endpoint because it opens a mobile contact page with an add/save contact button.

Do not use these older test endpoints for new NFC tags:

- `https://davidmolnar.dev/c`
- `https://davidmolnar.dev/contact`
- `https://davidmolnar.dev/contact.vcf`
- `http://127.0.0.1:4321/addcontact`

## Why URL-Based NFC

Direct vCard/contact records were considered and tested. They work better on Android, including offline cases, but iPhone background NFC reading is much more reliable with URL records.

The chosen flow is:

```text
NFC tag -> https://davidmolnar.dev/addcontact -> contact page -> save contact button
```

This keeps the physical tag stable and lets the website change the contact details or behavior later without rewriting tags or reprinting cards.

## Offline Tradeoff

URL-based NFC requires internet access. If offline contact saving becomes a requirement, the practical fallback is a separate vCard QR code or a direct vCard NFC tag, with the known downside that iPhone behavior is less reliable.

For this public version, the card prioritizes the cross-platform URL flow.

## Privacy Decision

Earlier NFC Tools screenshots contained private contact details, address information, and NFC tag serial data. Those screenshots must not be published.

The public repository intentionally keeps only the public-facing card identity, domain, and production contact endpoint.

## Original Design Attribution

This card is a customized derivative of:

- Original design: `Fancy Tech NFC Business Card - Fully Customizable`
- Designer: `EricP`
- Source: https://makerworld.com/hu/models/2335591-fancy-tech-nfc-business-card-fully-customizable#profileId-2554972

The current 3MF metadata includes `License: BY-SA`, so derivative design assets are published under CC BY-SA 4.0.
