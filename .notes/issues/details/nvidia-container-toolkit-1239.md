# NVIDIA/nvidia-container-toolkit Issue #1239

**URL**: https://github.com/NVIDIA/nvidia-container-toolkit/issues/1239  
**Title**: Wrong CDI spec creates error "Unresolvable CDI device"  
**Status**: Open  
**Created**: 2025-08-11  
**Updated**: 2025-08-11  
**Author**: @manuelbuil  
**Labels**: (none)  

---

## Original Issue Description

(Based on the GitHub page, user is experiencing a problem with NVIDIA Container Toolkit's CDI device generation):

- Using NVIDIA GPU Operator with RKE2 Kubernetes
- Container toolkit version is `v1.17.8`
- CDI is enabled with `cdi.enabled: true`
- When creating a pod with `runtimeClassName: nvidia-cdi`, it fails with an "Unresolvable CDI device" error

The key observation is that while `nvidia-smi` shows the GPU, the `/var/run/cdi/management.nvidia.com-gpu.yaml` file only contains a device named "all", not the specific GPU UUID.

The user manually ran `nvidia-ctk cdi generate` and saw three devices:
1. "0"
2. GPU-specific UUID  
3. "all"

They suspect the nvidia-container-toolkit is not correctly generating the CDI specification, despite logs showing it's attempting to generate the spec.

The user is seeking help to debug this issue and understand if additional configuration is needed in the operator or containerd configuration.

## Comments

(No comments yet on this issue as of the last check.)

## Technical Analysis

**Problem Type**: Container Device Interface (CDI) specification generation  
**Scope**: GPU device discovery and CDI spec creation  
**Impact**: Prevents GPU workloads from running in Kubernetes with CDI runtime

**Root Cause Hypothesis**:
- CDI spec generation logic may not be correctly enumerating all GPU devices
- Potential issue with RKE2/containerd integration
- Configuration mismatch between operator flags and CDI generation

## Viability Assessment

**Strengths**:
- Very recent issue (August 11, 2025) 
- Clear reproduction steps and environment details
- Specific error messages and diagnostic data provided
- Affects critical GPU container functionality

**Challenges**:
- Requires Kubernetes + containerd + CDI expertise
- Need access to NVIDIA GPU hardware for testing
- Complex integration between multiple systems (K8s, containerd, CDI, GPU drivers)

**Success Criteria**:
- CDI spec generation includes all GPU devices correctly
- Pods with `nvidia-cdi` runtime successfully access GPUs
- Manual and automatic CDI generation produce consistent results

## Implementation Approach

**Investigation Steps**:
1. Compare automatic vs manual CDI generation logic
2. Check device discovery code paths
3. Verify containerd/CDI integration
4. Test with different GPU configurations

**Potential Fixes**:
- Fix device enumeration in CDI generation
- Update operator configuration handling
- Improve error reporting for CDI issues

## Recommendation

This is a production-blocking issue for GPU containerized workloads. While it requires specialized knowledge of CDI and container runtimes, the problem is well-defined with clear success criteria. The issue is brand new (today) which suggests active user engagement and potential for quick maintainer response.