# Issues for NVIDIA/cccl

**Total Issues**: 174
**Repository**: https://github.com/NVIDIA/cccl

**Open Issues**: 100
**Closed Issues**: 74

---

## Issues List (Most Recently Updated First)

- **#5179: [EPIC] Use `cub::DeviceTransform` more widely in Thrust**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-11
  > `cub::DeviceTransform` offers a strong transform implementation by now. We should review Thrust's algorithms where it could be applied in addition to `thrust::transform` and then roll it out to more p...

- **#5196: Add  `cub::DeviceTransform::If` **
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-11
  > We should add a new conditional transform API to CUB with a predicate evaluated on the inputs which conditionally calls the transformation function and conditionally stores the result.

- **#5488: Port `thrust::transform_if` to `cub::DeviceTransform::TransformIf`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-11

- **#5397: [BUG]: cub::ScatterToStripedFlagged overload is calling the wrong function**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-08-11
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#4531: Enumerate Thrust features we want to pull into cuda:: namespace**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-11
  > - [ ] Algorithms - [ ] Containers - [ ] Utility Types   - type_traits:     - integer_sequence                           -> already an alias ✔      - is_contiguous_iterator                    -> should...

- **#874: [RFE] Use cudaLaunchKernel instead of <<<>>>**
  - Labels: cub
  - Comments: 5
  - Last updated: 2025-08-09
  > The main reason for this request is to improve error handling. When using <<<>>>, CUB currently has to call [cudaPeekAtLastError](https://github.com/NVIDIA/cub/blob/866c576c118ae036fb5c2759ba1e5997967...

- **#983: Add support for cmath**
  - Labels: libcu++
  - Comments: 5
  - Last updated: 2025-08-09
  > We should add support for `cmath` https://en.cppreference.com/w/cpp/header/cmath

- **#773: Remove redundant `reduce` implementation**
  - Labels: thrust
  - Comments: 1
  - Last updated: 2025-08-09
  > `thrust/system/cuda/detail/reduce.h` contains a complete reduction implementation in the `__reduce` namespace. In 8702bfe89640c9efcf68cf3ad2b89d4d00e96494, the `thrust::cuda_cub::reduce` entry points...

- **#969: asserts within library code should be opt-in not opt-out**
  - Labels: libcu++
  - Comments: 1
  - Last updated: 2025-08-09
  > assert within device code is relatively expensive. While users can opt-in to disabling asserts by defining NDEBUG optimzied builds should not have to define this to get performant library code.  Thi...

- **#965: C++20 std::numbers?**
  - Labels: libcu++
  - Comments: 1
  - Last updated: 2025-08-09
  > Hi! :wave:  Is there any roadmap describing planned support for newer, smaller headers? I want to use [std::numbers](https://en.cppreference.com/w/cpp/header/numbers) in my CUDA application, but NV...

- **#755: Test large types on QNX**
  - Labels: thrust
  - Comments: 1
  - Last updated: 2025-08-09
  > The `TestScanWithLargeTypes` test in `testing/scan.cu` skips large sizes for the QNX platform. We should see about re-enabling those.  ``` void TestScanWithLargeTypes(void) {   _TestScanWithLarge...

- **#941: Mirror docs to docs.nvidia.com**
  - Labels: libcu++
  - Comments: 1
  - Last updated: 2025-08-09
  > For SEO and integration with the CUDA Toolkit, we should have a CI job that pushes the Jekyll site for the docs to docs.nvidia.com. Pramod has done this before and can give us pointers.

- **#733: c++11 documentation**
  - Labels: thrust
  - Comments: 2
  - Last updated: 2025-08-09
  > I noticed that my thrust::shuffle documentation would not build by default because of the preprocessor flag `#if THRUST_CPP_DIALECT >= 2011`.   I want to make sure this documentation is available fo...

- **#710: thrust::device_delete cannot be compiled for class with user-defined constructor.**
  - Labels: thrust
  - Comments: 2
  - Last updated: 2025-08-09
  > Following code cannot be compiled:  ``` #include <thrust/device_ptr.h> #include <thrust/device_new.h> #include <thrust/device_delete.h>  struct Foo {      __host__ __device__ Foo() : x(0) {}...

- **#722: Why does thrust use `is_pod` to implement `has_trivial_destructor`?**
  - Labels: thrust
  - Comments: 1
  - Last updated: 2025-08-09
  > Hi all,  In https://github.com/thrust/thrust/blob/324243f6bb70687aeaeb2419193a335648c5869d/thrust/detail/type_traits.h#L177  The trait `has_trivial_destructor` is implemented as `is_pod`.  But in...

- **#721: THRUST_RUNTIME_FUNCTION uses __forceinline__**
  - Labels: thrust
  - Comments: 1
  - Last updated: 2025-08-09
  > This is probably over aggressive.

- **#855: Allow custom tuning policies to be passed into device algorithms.**
  - Labels: cub
  - Comments: 2
  - Last updated: 2025-08-09
  > When I used an iterator as an input for device-reduce reducing kernel was limited by amount of registers. The iterator does a few math operation on data in global memory plus branching. Degreasing def...

- **#694: deprecate "universal" iterator categories**
  - Labels: thrust
  - Comments: 4
  - Last updated: 2025-08-09
  > I don't think Thrust uses them, there's no reason for anyone else to, and they've always seemed hacky

- **#5484: `logical_device` and `green_context`: can we do better?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-08-09
  > Lately, I've been digging in cudax's and I found some inconsistencies.  I don't understand, why a non-owning wrapper for `physical_device`/`green_context` is called `logical_device`. I find it quite c...

- **#5327: [BUG]: Potentially uninitialized/oob reads of `vsmem` in `DeviceMergeSort`, `DeviceReduceByKey`, and `DeviceScanByKey`**
  - Labels: bug
  - Comments: 4
  - Last updated: 2025-08-09
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5479: c.parallel: replace hardcoded types in histogram with actual types passed by user**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-08
  > In `histogram.cu`, we currently instantiate `cub::detail::histogram::Transforms` with hardcoded types:  ```c++ cub::detail::histogram::Transforms<   LevelT, // LevelT   OffsetT, // OffsetT   LevelT //...

- **#4308: [EPIC]: Migrate cuCollections data structures to CCCL**
  - Labels: feature request
  - Comments: 6
  - Last updated: 2025-08-08
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5435: [BUG]: `GridEvenShare` does not work properly when `num_items == 0`.**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-08-08
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5427: Nondeterministic atomic reduce fails to compile when dtype is double for older architectures**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-08
  > `catch2_test_device_reduce_nondeterministic` fails to compile with `nvcc -arch=all` https://github.com/NVIDIA/cccl/actions/runs/16720645634/job/47324139613?pr=5398#step:4:1853. This is because the `do...

- **#5443: Nondeterministic reduce test fails on certain inputs**
  - Labels: cub
  - Comments: 2
  - Last updated: 2025-08-08
  > In a recent CI job, `cub.cpp20.test.device_reduce_nondeterministic.lid_0` failed initially but passed on a rerun (https://github.com/NVIDIA/cccl/actions/runs/16772255405/job/47492445253?pr=5414). ```...

- **#4601: Add python wrappers for histogram**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-07

- **#5297: [BUG]: `cub::DeviceMergeSort` intermittently causes `cudaErrorIllegalInstruction` likely due to `PDL` (Programmatic Dependent Launch)**
  - Labels: bug
  - Comments: 6
  - Last updated: 2025-08-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5344: [BUG]: `cub.cpp17.test.device_transform.lid_1` fails on GH200**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-08-07
  > Compiling and running the following test on GH200 (sm90): ``` cmake .. --preset=cub-cpp17 -DCMAKE_CUDA_ARCHITECTURES=native -B. ninja cub.cpp17.test.device_transform.lid_1 ./bin/cub.cpp17.test.device_...

- **#5124: Several Thrust unit tests fail for negative numbers**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-08-07
  > PR #4923 enables Thrust's unit testing framework to generate negative numbers. This lead to a lot of test failures, which require further investigation:  - [x] thrust.cpp.cuda.cpp20.test.cuda.sort.cdp...

- **#4922: Thrust unit test generators do not produce negative numbers**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-07
  > It turns out that the random number generators in Thrust's unit testing framework do not generate negative integers or floating points. This limits test coverage for an important range of inputs, as s...

- **#827: [DOC]: Use of horizontal space in Jekyll docs**
  - Labels: thrust
  - Comments: 2
  - Last updated: 2025-08-07
  > For a long time I was not sure what exactly I did dislike about the new documentation. I think the main problem is it's inefficient use of horizontal space.   E.g. looking at the [page about transfo...

- **#5453: [BUG]: Documentation for `thrust::cuda::par_nosync.on` missing**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-08-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5450: cccl.parallel: Replace `gpu_struct` with plain numpy struct types**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > https://github.com/NVIDIA/cccl/pull/3218 introduced the ability to use struct types as inputs to `cuda.cccl.parallel` algorithms.  As part of the design was a `@gpu_struct` decorator, which decorates...

- **#1947: [EPIC] Optimize `thrust::transform` for newer architectures**
  - Labels: thrust, cub
  - Comments: 3
  - Last updated: 2025-08-06
  > **Motivation** It's increasingly harder to reach SOL on newer GPU architectures, starting with A100 and H100, especially for simple kernels, like:  `thrust::transform(..., thrust::plus{})`, which basi...

- **#5367: [BUG]: DeviceReduce `gpu_to_gpu` determinism fallbacks to `run_to_run` determinism in unintended cases**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > ## Background  [https://github.com/NVIDIA/cccl/pull/2234](https://github.com/NVIDIA/cccl/pull/2234) and [https://github.com/NVIDIA/cccl/pull/4888](https://github.com/NVIDIA/cccl/pull/4888) PRs introdu...

- **#5449: Evaluate ast_canopy for auto-generating low-level Python cuda.coop interfaces**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06

- **#5448: Add CUDA 13 support for `cuda.cccl` Python package**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > Currently, the `cuda.cccl` Python package supports only CUDA 12. We need to support CUDA 13 as well.   Roughly speaking, the plan for this is to continue to ship a single `cuda.cccl` wheel, which will...

- **#1236: [BUG]: cuda::std::extents::static_extent truncates cuda::std::dynamic_extent when index_type is unsigned int**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-08-06
  > ### Is this a duplicate?  - [X] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5445: Redesign memory pool configuration API in cudax**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > I would like to converge on attributes being read-only and configuration being, well, configurable.  Currently in memory pool types in cudax we have `attribute` to query an attribute and `set_attribut...

- **#1626: Refactor `thrust/extrema.h` to use `cub::DeviceReduce`**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-08-06
  > _This is a sub-task of Thrust/CUB kernel consolidation https://github.com/NVIDIA/cccl/issues/26_ _Related: https://github.com/NVIDIA/cccl/issues/4475_  ### Prepare `cub::DeviceReduce` for feature pari...

- **#5444: Figure out how to expose an opt-in to calculate grid dimensions using a 32-bit type**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > Our hierarchy type has a default type per level type that is used for queries. It's unsigned int for all levels except `grid_level`, because grid dimensions can go up the range of an int, so the query...

- **#5339: Make sure the conforming preprocessor is used with MSVC in all CCCL tests**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > Basically check that `/Zc:preprocessor` is always specified to MSVC.

- **#5401: Refactor `thrust::reduce_by_key` to use `cub::DeviceReduce::ReduceByKey`**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-08-06
  > - [ ] https://github.com/NVIDIA/cccl/issues/5438 - [ ] Refactor `thrust::reduce_by_key` to use `cub::DeviceReduce::ReduceByKey`  - [ ] Add sanity tests for large number of items to thrust - [ ] Benchm...

- **#4208: [BUG]: `NV_IF_TARGET` is secretly a `NV_IF_ELSE_TARGET`**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-08-06
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2187: Create `cuda/type_traits` for `cuda::is_floating_point` trait**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-08-06

- **#5441: Generate `numeric_limits` for floating-point types from `__fp_xxx` values**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > Currently, we define `numeric_limits` for each floating point type separately. We should replace this by a single generic definition which should be implemented using our extended floating point infra...

- **#5438: Add support for virtual shared memory to `DispatchReduceByKey`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > This is a prerequisite for https://github.com/NVIDIA/cccl/issues/5401  - [x] Add support for virtual shared memory to `DispatchReduceByKey` - [x] Add CUB tests for vsmem helper - [x] Verify sass does...

- **#5374: [FEA]: Support windows build of `c.parallel`**
  - Labels: feature request
  - Comments: 2
  - Last updated: 2025-08-06
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5436: Make iterator `advance`, `dereference` and `op` functions accept arguments as `void*`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > Similar to the changes made for user-defined operators in https://github.com/NVIDIA/cccl/pull/4249, the iterator `advance`, `dereference` (and in the case of `TransformIterator`, user-provided `op`) d...

- **#5432: [FEA]: Runtime interface to query shared memory requirement**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-08-05
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5430: cuda.cccl.parallel: Reference examples in docstrings rather than tests**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-05
  > Right now, our docstrings reference tests from modules `test_<something>_api.py`. See for example:  https://github.com/NVIDIA/cccl/blob/aac401d582c80310fdd39015d802d95d9a1bf860/python/cuda_cccl/cuda/c...

- **#5425: c.parallel: radix sort tests do not use C2H**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04
  > The c.parallel tests were recently updated to use C2H, but it seems that `test_radix_sort.cpp` was missed. We need to update `test_radix_sort.cpp` to use C2H.

- **#5424: Single-phase: ensure temp_storage= works properly across all applicable algorithms**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04

- **#5423: Single-phase: figure out our documentation story (docstrings and higher-level docs)**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04

- **#5422: Single-phase: solution for argument validation and signatures/typing**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04
  > The validation of arguments such as items_per_thread etc. should be managed somewhere common and reused as much as possible.  Figure out the best way to handle both this validation, as well as ensurin...

- **#5421: Single-phase: ensure user-defined types work**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04

- **#5420: Single-phase: fix BlockPrefixCallbackOp (and other stateful operators)**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04

- **#5419: Investigate Performance of `deterministic DeviceReduce (RFA)` on `B200`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04
  > Recent benchmark's on **B200** of **deterministic DeviceReduce** i.e with `gpu_to_gpu` **determinism** showed that the performance is only 45% and 51% of SOL with F32 and F64 types respectively. But,...

- **#5351: Consolidate block_reduce_warp_reductions default and nondeterministic files**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04
  > Once https://github.com/NVIDIA/cccl/pull/4961 is merged, we should combine `block_reduce_warp_reductions.cuh` and `block_reduce_warp_reductions_nondeterministic.cuh` into a single file since they are...

- **#4600: [FEA]: Implement cccl.c.parallel version of histogram**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04

- **#5417: [STF] Fix DOT outputs and cleanup dot implementation**
  - Labels: stf
  - Comments: 0
  - Last updated: 2025-08-04
  > DOT outputs are currently broken, the task names are ignored   There are also calls like this in STF implementation, where we would rely on deduction instead  - dot.template add_vertex<typename Ctx::t...

- **#2131: [FEA]: Aynchronous data structures that use a cuda::mr::asyncresource to allocate their memory**
  - Labels: feature request, CUDA Next, 2.8.0
  - Comments: 0
  - Last updated: 2025-08-01
  > Stream ordered memory allocations a incredibly important for SOL applications.   At the same time they are easy to misuse. We need to provide uses with higher level data structures that minimize those...

- **#5340: [CUDAX] Make async_buffer work with host compilers**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-01
  > We should make sure `async_buffer` can be used without a CUDA compiler.  We should also consider dropping usage of Thrust inside it to make the symbols not depend on the target architectures when used...

- **#5119: Implement `BlockScan` overloads that invoke the `binary_op` only for the given `num_items`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-01
  > Today, most of the block-level algorithms have to be invoked with a full tile of items (i.e., `BLOCK_THREADS * ITEMS_PER_THREAD`). For these block-level algorithms, if users have problem sizes that ar...

- **#3942: [BUG]: The CUDA kernel of cub::DeviceReduce::ReduceByKey is likely slower than thrust::reduce_by_key**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-08-01
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5405: [FEA]: Headers that don't support NVRTC should emit diagnostic**
  - Labels: feature request, good first issue
  - Comments: 0
  - Last updated: 2025-07-31
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5404: [DOC]: Add special compatibility section for NVRTC**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-31
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#26: [EPIC] Consolidate kernels between Thrust and CUB**
  - Labels: feature request, thrust, cub
  - Comments: 2
  - Last updated: 2025-07-31
  > Below is a list of tasks in prioritized order. We should start with algorithms that already exist in CUB. This will allow delivering CUB optimizations into Thrust sooner.  ### Document procedure - [x]...

- **#265: [FEA]: Non-deterministic DeviceReduce**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-31
  > ### Is this a duplicate?  - [X] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5399: [FEA]: Migrate all cuco hasher's to cudax**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-31
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#1625: Refactor `thrust::unique` to use `cub::DeviceSelect::Unique`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-31
  > _This is a sub-task of Thrust/CUB kernel consolidation https://github.com/NVIDIA/cccl/issues/26_  ### Refactor `thrust::unique` to use `cub::DeviceSelect::Unique`: - [x] Make `thrust::unique` use `cub...

- **#5380: `cub::detail::WarpScanSmem` could be optimized/cleaned up**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-31
  > This is a rather low-priority issue given that this specialization of `cub::WarpScan` is only used for `LOGICAL_WARP_THREADS` is not a power of 2 which I assume is quite exotic. But while adding new m...

- **#5383: [BUG]: Silent failure in `cccl.parallel.reduce_into` when the input type does not match accumulator type**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-07-30
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5192: Implement `ThreadReduce` and `ThreadScan` alternatives that invoke the `binary_op` only for the given `valid_items`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-30
  > `BlockScan` member function overloads taking multiple items per thread use `ThreadReduce` and `ThreadScan[Inclusive, Exclusive]` to map the problem to the single-element overloads, so having alternati...

- **#5386: [FEA]: Provide Env-based API for cub::DeviceReduce::Select***
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-30
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5385: Add ZipIterator to `cuda.cccl.parallel`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-30
  > We need a `ZipIterator` in `cuda.cccl.parallel`, similar to https://nvidia.github.io/cccl/thrust/api/classthrust_1_1zip__iterator.html.  It should accept an arbitrary number of iterators as inputs. Us...

- **#5381: Investigate use of `cp.reduce.async.bulk` in histogram algorithms**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-29
  > The PTX instruction [`cp.reduce.async.bulk`](https://docs.nvidia.com/cuda/parallel-thread-execution/#data-movement-and-conversion-instructions-cp-reduce-async-bulk) can copy data back from shared memo...

- **#5378: [FEA]: Support for large offset type for deterministic DeviceReduce**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-28
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5333: Should `cub::DeviceReduce::Min/Max` and `cub::DeviceScan` without initial value require `cuda::std::numeric_limits<T>` to be specialized?**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-28
  > We recently ran into a bug where `cub::DeviceReduce::Min/Max` would produce the wrong result for a user defined type which did not specilize `cuda::std::numeric_limits<T>` (see #5264 and NVBug 5391162...

- **#5373: [FEA]: Add Windows CI Coverage for `cuda.cccl.parallel`**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-28
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#4968: Implement the standard formatting library and extensions**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-25
  > In #4939, I've already started porting libc++'s implementation of `std::format` to libcu++. This issue is intended to track the progress and discuss the changes.  The current design consists of severa...

- **#5320: cuda.cccl.parallel: Follow-up items for single-phase API implementation**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-25
  > A few follow-up items after #5207 is merged:  - [ ] For the object-based API, add named APIs to do temporary memory allocation and compute respectively, rather than using the first parameter to disamb...

- **#5370: [FEA]: The new single-phase API for cuda.cccl.parallel should have more checks on the input arrays**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-25
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5163: Simpler APIs for cuda.parallel**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-25
  > ## The problem - Python API is 3 phase  In C++, CUB APIs like `DeviceReduce` are invoked two times.  1. The first invocation computes temporary storage 2. The second invocation actually does the reduc...

- **#4388: Make c.parallel recognize well-known operations**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-24

- **#5366: c.parallel: investigate making ptx-json generate valid PTX**
  - Labels: CCCL-C
  - Comments: 0
  - Last updated: 2025-07-24
  > Currently, ptx-json emits invalid PTX, which means that regardless of whether we need to do a two C++ frontend pass compilation or not when building kernels, we have to do it. #5355 serves as a proof...

- **#5365: c.parallel: implement caching of transform configs**
  - Labels: CCCL-C
  - Comments: 0
  - Last updated: 2025-07-24
  > Currently, c.parallel's kernel source for transform disables caching of the runtime configs for transform; this creates a performance penalty every time transform is invoked. Incorporate the caching f...

- **#50: [EPIC]: CUB large input support**
  - Labels: feature request, cub, 2.8.0
  - Comments: 1
  - Last updated: 2025-07-24
  > As a lower-level interface, CUB should optimize for flexibility and performance. As a result, CUB will not guarantee a large input will work by default. However, it should enable users to specify thei...

- **#2520: Add support for large `num_items` to `DeviceRunLengthEncode::NonTrivialRuns`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-24
  > - [x] Implement tests for large number of items - [x] Evaluate benchmarks to check performance for different offset types - [x] Rewrite benchmarks to differentiate between `OffsetT` and `RunLengthT` -...

- **#4506: [FEA]: Expose transform UBLKCP algorithm via `cuda.parallel`**
  - Labels: feature request, cuda.parallel
  - Comments: 0
  - Last updated: 2025-07-24
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#4361: Refactor transform in c.parallel to use json magic for reusing CUB tuning policies**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-24

- **#5346: Investigate eliminating the need for two compilation calls re nvrtc.compile() for LTO/PTX**
  - Labels: 3.1.0
  - Comments: 1
  - Last updated: 2025-07-24

- **#4957: Implement new block histogram algorithm using cooperative groups.**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-07-23
  > Add a new algorithm (e.g. `cub::BlockHistogramAlgorithm::BLOCK_HISTO_CG`) that uses labeled cooperative-groups in conjunction with `atomicAdd` to potentially eliminate the number of atomics needed by...

- **#5345: Implement coop.block.histogram.**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-23
  > Bryce needs this for an upcoming training session on August 4th.

- **#5057: Make `cub::DeviceTransform` tunable**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-23
  > After the following changes land  - [x] #2394  - [x] #4976 - [x]  my internal rewrite of memcpy_async  land, we should make sure `cub::DeviceTransform` can be tuned.  Should include solving: #3017

- **#4606: Make CuPy an optional dependency**
  - Labels: cuda.parallel, cuda.cooperative
  - Comments: 0
  - Last updated: 2025-07-22
  > We are building fundamental libraries for all Python GPU libraries and frameworks such as CuPy, PyTorch, etc to depend on. So it is important that we do not make any of them a required dependency to a...

- **#997: Make `cuda::aligned_size_t` available in a more appropriate header than `<cuda/barrier>`**
  - Labels: libcu++
  - Comments: 8
  - Last updated: 2025-07-22
  > The [`cuda::aligned_size_t<N>`](https://github.com/NVIDIA/libcudacxx/blob/4f42427dfe5fd88672c29c279637e0ccf5b47478/include/cuda/std/barrier#L28-L36) type is currently defined in `<cuda/std/barrier>`....

- **#5321: Create a general abstraction for VSMemHelpers for c.parallel**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-21
  > Several CUB algorithms use VSMemHelper classes that have very similar structures between the algorithms. We should investigate if there's value in providing an abstraction to unify the handling of the...

- **#5308: Drop cupy as a dependency in cuda.cccl**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-21
  > Currently, cupy is used in a single place: to get the compute capability of the device (https://github.com/NVIDIA/cccl/blob/16751152ae45177f8a8802bbd742376925326c7b/python/cuda_cccl/cuda/cccl/parallel...

- **#5312: [FEA]: API for cuda/ptx jit compilation and linking**
  - Labels: feature request
  - Comments: 1
  - Last updated: 2025-07-19
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#4623: [BUG]: maybe add documentation about mixing thrust::device_vectors with different allocators**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-07-18
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2635: [DOC]: Create a CCCL developer guide**
  - Labels: doc
  - Comments: 4
  - Last updated: 2025-07-18
  > Developing CCCL involves a lot of conventions you have to be aware as a developer. Those conventions vary between different subprojects, but also a lot of commonalities (especially coming from libcu++...

- **#5294: [BUG]: `cuda::std::inplace_vector::at()` allows out of bounds access**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-07-17
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5266: [BUG]: CUB `DeviceRadixSort` and `DeviceMergeSort` silently fail**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-17
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5291: [STF] Ensure occupancy computation are properly cached**
  - Labels: bug, stf
  - Comments: 0
  - Last updated: 2025-07-17
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5290: Replace `THRUST_([HOST|DEVICE]_)FUNCTION` and maybe `CUB_RUNTIME_FUNCTION`**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-17
  > The use of these macros is mixed with `_CCCL_HOST_DEVICE` or `_CCCL_API`. We should consistently use CCCL macros instead of them and deprecate them. `CUB_RUNTIME_FUNCTION` seems to depend on `CUB_DISA...

- **#5289: [FEA]: Windows support for cuda.cccl Python package**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-17
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#4776: Investigate single-phase use of cuda.coop primitives.**
  - Labels: cuda.cooperative
  - Comments: 8
  - Last updated: 2025-07-16
  > Currently, in order to use the collective primitives in `cuda.cooperative`, a "two-phase" approach is required.  First, you obtain an `Invocable` from cuda.coop, specifying at minimum, the data type a...

- **#5280: Tagging and versioning in `main`**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-16
  > The versioning in `main` is confusing due to the way tagging is currently being done. Most tags are only reachable from the release branches, so as of this moment if I run `git desribe` on `main` I se...

- **#5282: [FEA]: Enable Windows GPU Testing**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-16
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5277: `_CCCL_SUPPRESS_DEPRECATED_PUSH` does not suppress warnings for NVRTC**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-16
  > If I configure and build the CCCL.C tests like: ``` cmake --preset cccl-c-parallel -DCMAKE_CUDA_ARCHITECTURES=native ninja cccl.c.parallel.test.transform.cpp ./bin/cccl.c.parallel.test.transform.cpp `...

- **#5030: make arch_traits accept enum instead of int**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-16
  > With the non-portable architecture features we might want to expose more than just the base portable architectures. We should change the architecture traits to be based on an enum instead of __CUDA_AR...

- **#5028: CCCL C fails to compile with g++-14**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-07-16
  > Reproduce with (using ToT CTK from yesterday on Ubuntu 25.04): ``` mkdir build_bug cd build_bug CXX=g++-14 cmake .. -DCMAKE_CUDA_HOST_COMPILER=/usr/bin/g++-14 -DCMAKE_CUDA_ARCHITECTURES=86 -DCUB_ENABL...

- **#5276: Revise `CMAKE_CUDA_ARCHITECTURES` used in `CMakePresets.json`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-16
  > Configuring with an internal CTK following CTK 12.9 I get: ``` cmake --preset cccl-c-parallel ... CMake Error at /usr/share/cmake-3.31/Modules/CMakeTestCUDACompiler.cmake:59 (message):   The CUDA comp...

- **#5275: `_CCCL_ASSERT` is not checked in CCCL.C unit tests when configured with RelWithDebInfo**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-16
  > `_CCCL_ASSERT` tests important assertions in host and device code and is thus always enabled in all unit tests. However, CCCL.C unit tests do not enable assertions when not built in cmake `Debug` mode...

- **#5203: [BUG]: `cuda::std::tuple_size_v<__half2>` fails**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-07-16
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5274: Reproducing failing Python CI runs does not work**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-16
  > I have a failing Python CI run on one of my PRs: https://github.com/NVIDIA/cccl/actions/runs/16314532468/job/46077941314?pr=4847. It tells me at the end that I can reproduce the issue by running: ```...

- **#5263: [BUG]: CUB `device_scan` and `device_reduce` failures on Blackwell**
  - Labels: bug, 3.0
  - Comments: 3
  - Last updated: 2025-07-16
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#4419: [FEA]: Complete overflow arithmetic**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-15
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5244: Use `thrust::transform` in `swap_ranges`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-15

- **#5226: [BUG]: size of tuple of tuples is not a sum of sizes of tuples**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-15
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5118: Support types with alignment > 16 in ublkcp DeviceTransform kernel**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-15

- **#5228: [BUG]: fp128 test and feature check are broken in v2.8.x & clang.**
  - Labels: bug
  - Comments: 5
  - Last updated: 2025-07-15
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5240: [FEA]: Provide namespace alias to `cuda::ptx` in `cuda::device`**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-15
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5257: [FEA]: Apply `__grid_constant__` wherever possible**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-14
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5171: Consider warning  when non-conforming MSVC preprocessor is used**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-14
  > MSVC has at least two preprocessor implementations: 1. the traditional one 2. the [standard conforming](https://learn.microsoft.com/en-us/cpp/preprocessor/preprocessor-experimental-overview?view=msvc-...

- **#5190: Refactor cccl.c merge sort to reuse tuning policies**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-14

- **#4362: Refactor unique_by_key in c.parallel to use json magic for reusing CUB tuning policies**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-14

- **#4359: Refactor scan in c.parallel to use json magic for reusing CUB tuning policies**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-14

- **#4364: Refactor RadixSort in c.parallel to use json magic for reusing CUB tuning policies**
  - Labels: CCCL-C
  - Comments: 0
  - Last updated: 2025-07-14

- **#4363: Refactor DeviceFor in c.parallel to use json magic for reusing CUB tuning policies**
  - Labels: CCCL-C
  - Comments: 0
  - Last updated: 2025-07-14

- **#5250: Use PDL in `cub::DeviceTransform`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-14

- **#3115: [EPIC] Use programmatic dependent launch in all CUB algorithms**
  - Labels: cub
  - Comments: 1
  - Last updated: 2025-07-14
  > [Programmatic dependent launch (PDL)](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#programmatic-dependent-launch-and-synchronization) allows subsequent kernels to skip a device-wide synchron...

- **#5245: Use `thrust::transform` in `uninitialized_copy[_n]`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-14

- **#4765: Add `cub::DeviceTransform::TransformIf`**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-14
  > CUB currently only has a 1:1 `transform` primitive, but lacks `transform_if` which skips writing to the output array if a predicate fails.  Such a primitive would also allow us to port `thrust::replac...

- **#5231: [FEA]: Implement segmented scans**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-13
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#3442: [FEA]: Expose a fast modulo division algorithm for device code**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-11
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#2553: [FEA]: Implement cuda.parallel version of segmented sort**
  - Labels: feature request
  - Comments: 1
  - Last updated: 2025-07-11
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#713: Document THRUST_DEBUG_SYNC**
  - Labels: thrust
  - Comments: 3
  - Last updated: 2025-07-11
  > The THRUST_DEBUG_SYNC ability to report the SM version of each executed algorithm is very useful in tracking down translation units compiled with mismatching SM versions.   Having formal documentati...

- **#718: thrust.github.io update (currently 2015 1.8.1 release listed as latest)**
  - Labels: thrust
  - Comments: 2
  - Last updated: 2025-07-11

- **#1137: [FEA]: Remove CDP (RDC) architecture filtering logic from Thrust/CUB tests**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-11
  > ### Is this a duplicate?  - [X] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#1138: [FEA]: Remove support for CDPv1 in Thrust algorithms **
  - Labels: feature request
  - Comments: 4
  - Last updated: 2025-07-11
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT...

- **#5120: Make cudax tests work on windows**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-10
  > We are working on setting up testing of cudax on Windows. We should first make sure the tests are working on that OS

- **#5019: Investigate the root causes in `DeviceScan` that lead to invalid values being passed to the custom reduction operator**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-07-09
  > ### Potential root causes (see https://github.com/NVIDIA/cccl/issues/5017): - [x] Handling and padding of out-of-bounds input items   - [x] Mathematical correctness of the `TailSegmentedReduce` implem...

- **#5193: [EPIC] Design user-defined tuning API for cuda.parallel algorithms**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-09
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5191: Implement `WarpScan` overloads that invoke the `binary_op` only for the given `num_items`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-09
  > `BlockScan` with `BLOCK_SCAN_WARP_SCANS` is based on `WarpScan`. So this is a prerequisite of #5119

- **#39: [FEA]: Multi-dimensional TMA exposure**
  - Labels: feature request, libcu++
  - Comments: 0
  - Last updated: 2025-07-08
  > There are a lot of extra, esoteric features in TMA that may not make sense for general CUDA C++ exposure. We will need to evaluate what we do and do not think is worth exposing.   - [ ] Define MVP fea...

- **#5125: List Thrust algorithms which could be implemented via `cub::DeviceTransform`**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-08
  > The following algorithms already use `cub::DeviceTransform`, directly or indirectly, today:  - `transform` - `transform_n` - `replace_copy_if`  These use `cub::DeviceTransform`, directly or indirectly...

- **#3188: [BUG]: Typo in set_difference documentation**
  - Labels: bug
  - Comments: 4
  - Last updated: 2025-07-08
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5166: [BUG]: compilation error**
  - Labels: bug
  - Comments: 7
  - Last updated: 2025-07-08
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5167: [FEA]: Optimize `BlockReduce`**
  - Labels: feature request, cub
  - Comments: 0
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5165: [BUG]: cannot compile since CUDA 12.9**
  - Labels: bug
  - Comments: 2
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2323: [DOC]: Clarity check of CUB device-scope docs**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2325: [DOC]: Clarity check of CUB warp-scope docs**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2319: Return algorithm diagrams to CUB docs**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-07
  > We used to have algorithm diagrams in CUB docs. For instance, reduction used to have the following picture:  ![Image](https://github.com/user-attachments/assets/67450dca-68ac-4318-b80e-0c05997fe9e0)...

- **#2324: [DOC]: Clarity check of CUB block-scope docs**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2321: [DOC]: Investigate docs grouping automation**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2237: [FEA]: `sccache` should be a purely optional dependency in CCCL's build scripts**
  - Labels: feature request
  - Comments: 6
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [X] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT...

- **#2320: [DOC]: Group cuda.cooperative docs**
  - Labels: doc
  - Comments: 0
  - Last updated: 2025-07-07
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#913: Optimise decoupled look-back for small non-primitive types**
  - Labels: cub
  - Comments: 1
  - Last updated: 2025-07-07
  > For primitive types, the decoupled look-back combines the two memory transactions of (1) updating the tile's status (e.g., `partial`, `inclusive`) and (2) updating the tile's value. This is a welcome...

- **#5018: Write a `DeviceScan` test case that fails when an invalid value is passed to the custom reduction operator**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-07
  > We need a test case that fails when invalid values are passed to the reduction operator in `DeviceScan`. Specifically, we want to write a test that makes sure that, for both parameters passed to the r...

- **#5116: [BUG]: `cuda::std::copy()` uses unqualified `__unwrap_iter()`, which is ambiguous with LLVM libc++'s equivalent definition**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-07-06
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5137: `_CCCL_SUPPRESS_DEPRECATED_PUSH` is not strong enough**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-06
  > `_CCCL_SUPPRESS_DEPRECATED_PUSH` is intended to begin a region where deprecation warnings are suppressed. However, occasionally deprecation warnings still escape a region of: ``` _CCCL_SUPPRESS_DEPREC...

- **#5160: [EPIC] Add missing Thrust algorithms**
  - Labels: help wanted
  - Comments: 0
  - Last updated: 2025-07-04
  > Thrust currenty misses implementations for the following algorithms operating on ranges of elements. Based on C++23.  From the `<algorithm>` header:  - [ ] find_end(I, I, I, I)  - [ ] find_end(I, I, I...

- **#5159: [BUG]: c.parallel unit tests link c2h (with THRUST_DEVICE_SYSTEM=CUDA) but compile without a CUDA compiler**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-07-04
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#5152: Use cases of scan algorithms worth benchmarking**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-04
  > Scan algorithm with `std::plus` operator is known as [cumulative sum](https://www.mathworks.com/help/matlab/ref/double.cumsum.html). It is standardized in [Python Array API](https://data-apis.org/arra...

- **#5157: The internal Thrust sequential system should be replaced by libcu++**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-04
  > Thrust maintains a large implementation of [sequential algorithms](https://github.com/bernhardmgruber/cccl/blob/3314a70aa01e477c8f645da810e9810002f80483/thrust/thrust/system/detail/sequential). These...

- **#5142: [BUG]: Several members of `cuda::std::inplace_vector` are not `static` when they should be.**
  - Labels: bug
  - Comments: 1
  - Last updated: 2025-07-04
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#2938: [FEA]: `cuda::span_collection`**
  - Labels: feature request
  - Comments: 1
  - Last updated: 2025-07-03
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#5103: Updating RAPIDS CI to use CUDA 12.9**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-03
  > RAPIDS 25.08 is upgrading to CUDA 12.9. It looks like CCCL already has added CUDA 12.9 to CI.  As a next step think we can now update to CUDA 12.9 in CCCL's RAPIDS CI. Filing this issue to track.  Ref...

- **#5144: [BUG]: cuda.cccl.parallel algorithms do not support cuda.core.experimental.Stream**
  - Labels: bug
  - Comments: 3
  - Last updated: 2025-07-03
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this bug and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.md)...

- **#4960: [FEA]: Provide Env-based API for cub::DeviceReduce::Sum**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-03
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

- **#4886: Enable ability to have a Catch2 test alongside libcudacxx lit tests**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-07-02
  > As we productize things from `cuda::experimental` and move the headers, we'll need to migrate their tests as well.  These tests are written in Catch2 and not lit and we don't want to rewrite Catch2 te...

- **#5127: [FEA]: Add ability for user to control nvtx range names through execution policy**
  - Labels: feature request
  - Comments: 0
  - Last updated: 2025-07-02
  > ### Is this a duplicate?  - [x] I confirmed there appear to be no [duplicate issues](https://github.com/NVIDIA/cccl/issues) for this request and that I agree to the [Code of Conduct](CODE_OF_CONDUCT.m...

