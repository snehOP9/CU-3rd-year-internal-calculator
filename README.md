# CU 3rd Year CSE Total Internal Calculator

A modern, responsive internal marks calculator for Chandigarh University CSE 3rd year students.

## Features

- Subject-wise dynamic scheme mapping (Theory / Hybrid / Practical / Not Configured)
- Exact formula implementation for each configured subject type
- Inline validation for every field with max marks constraints
- Live summary panel with total entered marks, max marks, scaled marks, and final result
- Dark/light theme toggle
- Copy result summary
- Export/Print via browser print flow
- Local storage persistence for selected subject, entered values, and theme

## Tech

- HTML5
- CSS3 (glassmorphism, responsive layout, transitions)
- Vanilla JavaScript (data-driven config + dynamic rendering)

## Run

1. Open `index.html` in a browser.
2. Select a subject.
3. Enter marks in visible fields.
4. Use **Calculate** for final result card.

No build tools required.

## Project Structure

- `index.html` → UI, styling, configuration, formulas, validation, and interactivity
- `README.md` → project documentation

## Notes

- `Aptitude-IV (23TDT-362)` is intentionally marked as not configured.
- Final values are rounded to 2 decimal places.
- Practical final output is shown on a `/ 60` scale based on formula `((Experiments/300)*45) + Mid-Term`.

## Optional Future Improvements

- PWA install support
- Multi-semester profile support
- PDF layout customization beyond print dialog
- Backend sync for saved attempts
