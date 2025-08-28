# Top 3 Viable Issues - Sage Carbon Repository

## Analysis Date: August 28, 2025

Based on analysis of the issue tickets in the sage_carbon directory, here are the top 3 most viable issues to solve, prioritizing technical implementation over documentation tickets.

---

## 1. Issue #7486 - Form height not applied due to child `<div>`
**Priority: HIGH**  
**Complexity: LOW**  
**Date Opened:** 2025-08-14

### Issue Details
- **Link:** https://github.com/Sage/carbon/issues/7486
- **Type:** Bug
- **Status:** On Backlog, Squad Megabat
- **Reproduction:** https://stackblitz.com/edit/parsium-carbon-starter-moagdatx

### Problem Description
The Form component's `height` prop is not being respected because the direct child `<div>` element with data-role "form-content" has no styles applied. This causes the height to be determined by content rather than the specified prop value.

### Viability Assessment
- **Clear Fix Path:** Add CSS height inheritance to the form-content div
- **Low Risk:** CSS-only change with minimal side effects
- **Has Reproduction:** Stackblitz demo available for testing
- **Impact:** Affects all Form components using height prop

### Implementation Approach
```css
/* Apply height: 100% or height: inherit to form-content div */
[data-role="form-content"] {
  height: 100%;
}
```

---

## 2. Issue #7497 - MenuItem: styles are not consistently computed
**Priority: HIGH**  
**Complexity: MEDIUM**  
**Date Opened:** 2025-08-20

### Issue Details
- **Link:** https://github.com/Sage/carbon/issues/7497
- **Type:** Bug  
- **Status:** On Backlog
- **Version Regression:** Works in v155.9.1, broken in v155.10.0

### Problem Description
CSS rules are applied in different order between versions, causing padding misalignment in MenuItem components. The padding: 11px 16px 10px is overridden differently between versions.

### Viability Assessment
- **Root Cause Clear:** CSS specificity/ordering issue
- **Version-Specific:** Regression between specific versions helps narrow the cause
- **Visual Impact:** Directly affects UI appearance
- **Has Stackblitz:** Attempt provided (though not fully reproducible)

### Implementation Approach
- Review CSS build process changes between v155.9.1 and v155.10.0
- Ensure consistent specificity for MenuItem padding rules
- Consider using more specific selectors or !important as temporary fix

---

## 3. Issue #7469 - Message doesn't appear to be focusable as docs suggest
**Priority: MEDIUM**  
**Complexity: LOW-MEDIUM**  
**Date Opened:** 2025-07-30

### Issue Details
- **Link:** https://github.com/Sage/carbon/issues/7469
- **Type:** Bug
- **Status:** On Backlog
- **Documentation:** https://carbon.sage.com/iframe.html?viewMode=docs&id=message--docs

### Problem Description
The Message component accepts a ref but doesn't properly forward it to a focusable element. The ref is passed to Message.style styled component which doesn't handle it, breaking the documented focus functionality.

### Viability Assessment
- **Clear Bug:** Ref forwarding not working as documented
- **Straightforward Fix:** Forward ref to the dismiss button or wrapper
- **Accessibility Impact:** Affects keyboard navigation
- **Well-Defined Scope:** Limited to Message component ref handling

### Implementation Approach
```javascript
// Forward ref to the IconButton (dismiss button) or wrapper element
// Current: ref -> Message.style (does nothing)
// Fix: ref -> IconButton or focusable wrapper
```

---

## Honorable Mentions

### Issue #7486 - Form Height (Alternative consideration)
While listed as #1, this could also be considered alongside:

### Issue #7483 - Background enabled when Responsive Vertical Menu is open
- **Complexity:** MEDIUM-HIGH (requires focus trap implementation)
- **Impact:** Significant accessibility issue
- **Status:** Has ongoing design discussion

### Issue #6942 - Focus ring z-index issue in FlatTable
- **Complexity:** LOW (CSS z-index fix)
- **Impact:** Visual bug affecting focus indicators
- **Age:** Older issue from September 2024

---

## Recommendation Summary

The top 3 issues selected offer:
1. **Quick wins** with clear implementation paths
2. **Recent issues** (mostly from 2025) showing active problems
3. **Reproducible bugs** with stackblitz demos or clear descriptions
4. **Non-breaking fixes** that won't require major refactoring

Start with Issue #7486 (Form height) as it's the simplest CSS fix, then tackle #7497 (MenuItem styles) which requires more investigation but has clear regression points, and finally #7469 (Message focus) which improves accessibility.