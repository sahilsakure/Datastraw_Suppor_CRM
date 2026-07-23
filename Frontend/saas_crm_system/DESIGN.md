---
name: SaaS CRM System
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434655'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#943700'
  on-tertiary: '#ffffff'
  tertiary-container: '#bc4800'
  on-tertiary-container: '#ffede6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#7d2d00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-sm:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 32px
---

## Brand & Style
The brand personality is professional, efficient, and reliable. It is designed for high-density customer support environments where clarity and speed of information processing are paramount. The design style follows a **Modern Corporate/Minimalist** approach, prioritizing functional utility over decorative elements.

The UI should evoke a sense of calm control through heavy whitespace, a restricted color palette, and high-quality typography. It avoids visual clutter, ensuring that complex CRM data remains approachable and easy to navigate for support agents.

## Colors
The palette is built on a "Crisp White" foundation to maximize readability and reduce eye strain. 

- **Primary:** Deep Blue (#2563eb) is reserved for primary actions, active states, and critical focal points.
- **Secondary/Text:** Slate Grays (#475569) provide hierarchy for secondary text and structural borders.
- **Surface:** A neutral off-white (#f8fafc) is used for background layering to separate the navigation from the main workspace.
- **Feedback:** Use standard success (Emerald 600), warning (Amber 500), and error (Rose 600) tokens sparingly to maintain the professional tone.

## Typography
This design system utilizes **Inter** for its systematic, utilitarian nature. The scale is optimized for SaaS interfaces where data density is high. 

- **Headlines:** Use semi-bold weights with slight negative letter-spacing for a modern, "tight" look.
- **Body:** The default size is 14px (`body-md`) for internal dashboards to maximize the information visible on-screen.
- **Labels:** Use `label-sm` in all-caps or bold weights for table headers and form labels to provide clear structural scaffolding.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model. The sidebar navigation remains fixed at 280px, while the main content area fluidly expands to fill the viewport, capped at a maximum width of 1600px for readability.

- **Grid:** Use a 12-column grid for dashboard widgets and form layouts.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Density:** Provide 16px of padding inside cards and 24px of gutter space between major layout sections to maintain the "generous whitespace" requirement.

## Elevation & Depth
The system uses **Tonal Layers** combined with **Ambient Shadows** to define hierarchy. 

- **Level 0 (Background):** Solid white or #f8fafc.
- **Level 1 (Cards/Panels):** White background with a 1px border (#e2e8f0) and a very soft, diffused shadow (0px 1px 3px rgba(0,0,0,0.05)).
- **Level 2 (Dropdowns/Modals):** White background with a more pronounced shadow (0px 10px 15px -3px rgba(0,0,0,0.1)) to indicate clear interaction priority.
- **Interactive:** Hover states on buttons and list items should use subtle background color shifts rather than shadow changes.

## Shapes
The shape language is consistently **Rounded**. 
- Standard components (buttons, inputs, cards) use a base radius of **8px**. 
- Larger containers like main dashboard panels use **12px** to soften the professional aesthetic.
- Avatars and status "pills" use a full circular radius for distinct shape contrast against the rectangular grid.

## Components

### Buttons
- **Primary:** Solid #2563eb with white text. 8px corner radius.
- **Secondary:** White background with #e2e8f0 border and #475569 text.
- **Ghost:** No background or border, used for utility actions in table rows.

### Data Tables
- **Header:** #f8fafc background, 12px semi-bold slate text, 1px bottom border.
- **Rows:** 56px minimum height, subtle #f8fafc hover state.
- **Cells:** Vertical alignment centered; 14px text.

### Form Inputs
- **Default:** 1px border (#e2e8f0), 8px radius, 12px horizontal padding.
- **Focus State:** 1px #2563eb border with a 3px soft blue outer glow.
- **Labels:** 14px Medium weight Slate Gray, positioned 8px above the input.

### Navigation Bars
- **Sidebar:** Darker slate or very light gray background to distinguish from content. Active links should feature a 4px vertical primary-blue bar on the left edge.
- **Top Bar:** 64px height, blurred white background, containing breadcrumbs and global search.

### Chips/Badges
- Small 12px text, 24px height, semi-rounded. Use light tinted backgrounds (e.g., light blue background with dark blue text) for status indicators.