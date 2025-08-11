# NVIDIA/cccl Issue #5327

**URL**: https://github.com/NVIDIA/cccl/issues/5327  
**Title**: [BUG]: Potentially uninitialized/oob reads in DeviceMergeSort, DeviceReduceByKey, and DeviceScanByKey  
**Status**: Open  
**Created**: 2025-08-08  
**Updated**: 2025-08-09  
**Labels**: bug  

---

## Original Issue Description

### Is this a duplicate?

- [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)

### Type of Bug

Something else

### Component

CUB

### Describe the bug

After https://github.com/NVIDIA/cccl/pull/5260 was merged, we started seeing `compute-sanitizer --tool initcheck` complain about uninitialized memory reads. E.g.,

https://github.com/NVIDIA/cccl/actions/runs/16397743192/job/46333472060#step:4:2919

Affected algorithms are `DeviceMergeSort`, `DeviceReduceByKey`, and `DeviceScanByKey`. 

We want to investigate whether these are UB or whether they may cause actual functional regressions.

### How to Reproduce

Run under `compute-sanitizer --tool initcheck`:
- vsmem tests for `DeviceMergeSort`
- `DeviceReduceByKey` and `DeviceScanByKey` tests 

### Expected behavior

No uninitialized memory reads should be reported.

### Additional information

The specific failing job can be run by defining the override matrix in `ci/matrix.yaml` to:

```
 - {jobs: ['compute_init_lid0'], project: 'cub', std: 'max', gpu: 'rtxa6000', sm: 'gpu', cmake_options: '-DCMAKE_CUDA_FLAGS=-lineinfo'}
```

from a PR. Check that this job is passing before merging the fix.

## Comments (Exact Text)

### Comment 1 by bernhardmgruber (July 22, 2025):
"Wait, so `thrust::no_init` that scared some folks for its potential to introduce bugs, is now actually discovering bugs? Amazing plot twist! :D"

### Comment 2 by bernhardmgruber (July 22, 2025):
> We want to investigate whether these are UB or whether they may cause actual functional regressions.

"Frankly, a read of uninitialized memory is always UB and we should try hard to avoid it. But I may understand that if there is no functional impact, we may address it with less priority."

### Comment 3 by alliepiper (July 22, 2025):
"FYI, The failing job can be replicated in GH CI by adding this to the override matrix of a PR:"

```
 - {jobs: ['compute_init_lid0'], project: 'cub', std: 'max', gpu: 'rtxa6000', sm: 'gpu', cmake_options: '-DCMAKE_CUDA_FLAGS=-lineinfo'}
```

"I'll add this to the repro information."

### Comment 4 by elstehle (August 9, 2025):
[Detailed technical investigation of uninitialized memory reads in different algorithms, including analysis of compute-sanitizer output and specific code lines that might be causing the issue. This comment provides in-depth technical details about potential uninitialized memory reads in DeviceMergeSort, DeviceReduceByKey, and DeviceScanByKey algorithms.]

## Technical Analysis

**Severity**: High - Memory safety bug affecting core GPU algorithms  
**Scope**: Multiple CUB device algorithms  
**Root Cause**: Bounds checking and memory initialization issues  

## Viability Assessment

**Strengths**:
- Clear technical scope (specific algorithms identified)
- Active maintainer engagement (elstehle investigation)
- Detailed reproduction steps provided
- Memory safety issues typically have well-defined fixes

**Challenges**:
- Requires CUDA/GPU programming expertise
- Complex memory management debugging
- Need access to NVIDIA GPU hardware for testing

**Success Criteria**:
- Passes compute-sanitizer memory checks
- No functional regressions in affected algorithms
- Proper bounds checking implementation

## Recommendation
I
This is a high-priority memory safety issue in critical GPU computing infrastructure. The technical scope is well-defined and maintainers are actively engaged. However, it requires specialized CUDA development skills and GPU testing environment.