# stripe/react-stripe-js Issue #603

**URL**: https://github.com/stripe/react-stripe-js/issues/603  
**Title**: [BUG]: The `on` method of the `useCheckout()` function is omitted, yet it is utilised in the provided quickstart example  
**Status**: Open  
**Created**: 2025-07-21  
**Updated**: 2025-08-11  
**Author**: @tomgreef  
**Labels**: bug, stale  

---

## Original Issue Description

(I need to get the exact original text from the issue author. Let me fetch it directly.)

## Technical Analysis

**Problem Type**: API inconsistency between documentation and implementation  
**Scope**: Single method (`on`) in `useCheckout()` function  
**Impact**: Developers following quickstart guide encounter broken code

## Code Reference
The issue specifically mentions:
- **File**: `CheckoutForm.jsx` 
- **Line**: 59
- **Method**: `.on()` method usage

## Viability Assessment

**Strengths**:
- Clear, well-defined problem scope (single missing method)
- Documentation inconsistency is straightforward to fix
- Recent activity (updated August 11, 2025)
- Repository is well-maintained (only 6 open issues total)

**Implementation Options**:
1. **Add the method back**: Restore `on` method to TypeScript definitions
2. **Update documentation**: Remove `on` method usage from quickstart
3. **Provide alternative**: Show correct event handling approach

**Success Criteria**:
- Either method works in quickstart example, or documentation is updated
- TypeScript definitions match actual API functionality
- Developers can successfully follow the quickstart guide

## Recommendation

This is an excellent candidate for contribution because:
- **Low complexity**: Documentation/API consistency issue
- **Clear scope**: Single method in well-defined context
- **High developer impact**: Affects new user onboarding
- **Well-maintained repo**: Only 6 open issues, active maintenance

The fix could involve either restoring the method or updating documentation - both are straightforward changes.