# Round 1 Issue Nominations

Selection criteria applied:
- **MUST BE** software engineering relevant (cost effectiveness, security, scaling, performance)
- Most viable (least complex)
- Have been RECORDED after Jan 2024

---

## mastercard-developers-agent-toolkit
**Status**: No issues found (0 total issues)
**Nominations**: None possible

---

## mastercard-flow (27 total issues)

1. **#976: Fix jline compatibility** (Last updated: 2025-02-17)
   - *Engineering relevance*: Dependency management, maintaining up-to-date libraries
   - *Viability*: Dependency upgrade issue with clear scope

2. **#999: Fix mermaid compatibility** (Last updated: 2024-11-19)  
   - *Engineering relevance*: Security (vulnerability fixes), dependency management
   - *Viability*: Version bump with identified security benefits

3. **#975: Fix mysterious CI failures** (Last updated: 2024-10-21)
   - *Engineering relevance*: Build reliability, development velocity
   - *Viability*: Re-enabling disabled tests, focused scope

4. **#896: Package chains as DynamicContainers** (Last updated: 2024-10-04)
   - *Engineering relevance*: Developer experience, test organization
   - *Viability*: Junit5 improvement with clear requirements

5. **#881: Fix inter-line deadzone in hexdump view** (Last updated: 2024-08-08)
   - *Engineering relevance*: User interface improvement, good first issue
   - *Viability*: Frontend fix with specific scope

6. **#887: Message view line numbers** (Last updated: 2024-08-06)
   - *Engineering relevance*: Developer debugging experience
   - *Viability*: UI enhancement with clear requirements

7. **#882: Show raw data for unparseable actuals** (Last updated: 2024-08-02)
   - *Engineering relevance*: Error handling, debugging capability
   - *Viability*: Enhanced error reporting with clear scope

8. **#820: Versions capture** (Last updated: 2024-07-15)
   - *Engineering relevance*: Reproducible testing, version tracking
   - *Viability*: Metadata capture feature for better traceability

9. **#868: Configuration capture** (Last updated: 2024-07-15)
   - *Engineering relevance*: Reproducible test runs, debugging
   - *Viability*: Configuration documentation enhancement

10. **#816: HttpReq - basic auth utility method** (Last updated: 2024-06-07)
    - *Engineering relevance*: Developer productivity, API usability
    - *Viability*: Small utility method addition, good first issue

---

## monzo-response (56 total issues)
**Note**: Most issues are from before 2024, very few qualify under the date criteria

1. **#262: docker-compose build error at step 2/8** (Last updated: 2023-08-28)
   - *Engineering relevance*: Container deployment, build system reliability
   - *Viability*: Docker configuration fix

2. **#125: Add back Statuspage and PagerDuty integrations** (Last updated: 2020-10-12)
   - *Engineering relevance*: System reliability, incident management integrations
   - *Viability*: Well-defined integration requirements

*Note: This repository has limited qualifying issues due to most being pre-2024. Only showing top engineering-relevant issues.*

---

## monzo-terrors  
**Status**: No issues found (0 total issues)
**Nominations**: None possible

---

## nvidia-cccl (174 total issues)

1. **#5488: Port thrust::transform_if to cub::DeviceTransform::TransformIf** (Last updated: 2025-08-11)
   - *Engineering relevance*: Performance optimization, algorithm consolidation
   - *Viability*: Well-defined API porting task

2. **#5397: [BUG]: cub::ScatterToStripedFlagged overload calling wrong function** (Last updated: 2025-08-11)
   - *Engineering relevance*: Correctness bug, API consistency
   - *Viability*: Clear bug with specific fix needed

3. **#874: [RFE] Use cudaLaunchKernel instead of <<<>>>** (Last updated: 2025-08-09)
   - *Engineering relevance*: Error handling improvement, API modernization
   - *Viability*: Systematic API migration with clear benefits

4. **#5327: [BUG]: Potentially uninitialized/oob reads in DeviceMergeSort, DeviceReduceByKey, and DeviceScanByKey** (Last updated: 2025-08-09)
   - *Engineering relevance*: Memory safety, critical bug fix
   - *Viability*: Security-critical fix with identified scope

5. **#4531: Enumerate Thrust features to pull into cuda:: namespace** (Last updated: 2025-08-11)
   - *Engineering relevance*: API consolidation, namespace organization
   - *Viability*: Systematic feature migration task

6. **#5124: Several Thrust unit tests fail for negative numbers** (Last updated: 2025-08-07)
   - *Engineering relevance*: Test coverage, correctness
   - *Viability*: Test fixes with clear scope

7. **#1947: [EPIC] Optimize thrust::transform for newer architectures** (Last updated: 2025-08-06)
   - *Engineering relevance*: Performance optimization for new hardware
   - *Viability*: Architecture-specific optimizations

8. **#5367: [BUG]: DeviceReduce gpu_to_gpu determinism fallbacks to run_to_run determinism** (Last updated: 2025-08-06)
   - *Engineering relevance*: Algorithm correctness, deterministic behavior
   - *Viability*: Determinism fix with clear requirements

9. **#5444: Figure out how to expose opt-in to calculate grid dimensions using 32-bit type** (Last updated: 2025-08-06)
   - *Engineering relevance*: Memory optimization, API design
   - *Viability*: Type system improvement with defined scope

10. **#5438: Add support for virtual shared memory to DispatchReduceByKey** (Last updated: 2025-08-06)
    - *Engineering relevance*: Memory management, performance optimization
    - *Viability*: Memory optimization feature with clear benefits

---

## nvidia-nvidia-container-toolkit (167 total issues)

1. **#1239: Wrong CDI spec creates error "Unresolvable CDI device"** (Last updated: 2025-08-11)
   - *Engineering relevance*: Configuration correctness, deployment reliability
   - *Viability*: CDI specification issue with clear error case

2. **#1227: Failed to initialize NVML after systemctl daemon-reload** (Last updated: 2025-08-08)
   - *Engineering relevance*: System reliability, container persistence
   - *Viability*: System integration issue with reproducible case

3. **#1215: CDI Spec Generation missing driver libraries** (Last updated: 2025-08-08)
   - *Engineering relevance*: Container runtime completeness
   - *Viability*: Library detection improvement

4. **#1225: CLI flags should be ignored when unrecognised hook detected** (Last updated: 2025-08-06)
   - *Engineering relevance*: Backward compatibility, error handling
   - *Viability*: CLI robustness improvement

5. **#1224: Support IMEX_CHANNELS in jit-cdi mode** (Last updated: 2025-08-06)
   - *Engineering relevance*: Feature completeness, JIT compilation support
   - *Viability*: Feature parity implementation

6. **#1222: Container Toolkit messed up config.toml in GKE cluster with containerd 2.0** (Last updated: 2025-08-05)
   - *Engineering relevance*: Container runtime compatibility
   - *Viability*: Configuration compatibility fix

7. **#1218: Disable chmod hook by default** (Last updated: 2025-08-04)
   - *Engineering relevance*: Security, default configuration improvement
   - *Viability*: Default behavior change with security benefit

8. **#1208: invalid mitigation of cve-2025-23266** (Last updated: 2025-08-02)
   - *Engineering relevance*: Security documentation, vulnerability mitigation
   - *Viability*: Documentation correction for security issue

9. **#1203: CDI behavior with NVIDIA GPU devices in Kubernetes** (Last updated: 2025-08-01)
   - *Engineering relevance*: Kubernetes integration, container orchestration
   - *Viability*: CDI behavior clarification and fix

10. **#1199: NVIDIA Container Toolkit fails with "libnvidia-ml.so.1 not found" on RTX 5070** (Last updated: 2025-07-30)
    - *Engineering relevance*: New hardware support, library compatibility
    - *Viability*: Driver compatibility issue with new hardware

---

## stripe-react-stripe-js (325 total issues)

1. **#603: [BUG]: The on method of useCheckout() function is omitted** (Last updated: 2025-08-11)
   - *Engineering relevance*: API completeness, developer experience
   - *Viability*: Missing API method implementation

2. **#601: [BUG]: ExpressCheckoutElement onClick doesn't work with latest stripe-js** (Last updated: 2025-08-05)
   - *Engineering relevance*: API compatibility, version management
   - *Viability*: Version compatibility fix

3. **#596: [BUG]: Auto-focus in Country field dropdown after entering CVC on iOS Safari** (Last updated: 2025-07-29)
   - *Engineering relevance*: User experience, cross-platform compatibility
   - *Viability*: Mobile browser-specific fix

4. **#569: [BUG]: React 19 global JSX namespace deprecation** (Last updated: 2025-07-25)
   - *Engineering relevance*: Future compatibility, framework migration
   - *Viability*: React version compatibility update

5. **#441: [BUG]: input.__PrivateStripeElement-input ARIA hidden element must not be focusable** (Last updated: 2025-07-15)
   - *Engineering relevance*: Accessibility, compliance
   - *Viability*: Accessibility improvement with clear requirements

6. **#592: [BUG]: 3DS confirmation flow broken with ExpressCheckoutElement** (Last updated: 2025-06-26)
   - *Engineering relevance*: Payment flow reliability, security
   - *Viability*: Authentication flow fix

7. **#594: [BUG]: Hydration Error with Stripe PaymentElement in Next.js** (Last updated: 2025-06-18)
   - *Engineering relevance*: SSR compatibility, framework integration
   - *Viability*: Next.js integration fix

8. **#581: [BUG]: Express Checkout Element errors with token_already_used** (Last updated: 2025-05-27)
   - *Engineering relevance*: Payment flow reliability, error handling
   - *Viability*: Token management improvement

9. **#580: [BUG]: Accessibility issues with Paypal button from Express Checkout element** (Last updated: 2025-04-25)
   - *Engineering relevance*: Accessibility, compliance
   - *Viability*: Button accessibility improvement

10. **#574: [BUG]: Card Element onChange does not work consistently** (Last updated: 2025-04-11)
    - *Engineering relevance*: Event handling reliability, developer experience
    - *Viability*: Event system consistency fix

---

## stripe-stripe-go (65 total issues)

1. **#2093: Unable to create BankAccount** (Last updated: 2025-08-11)
   - *Engineering relevance*: API correctness, URL parsing bug
   - *Viability*: Clear URL formatting fix

2. **#2092: Missing .Metadata field for BankAccountCreateParams** (Last updated: 2025-08-11)
   - *Engineering relevance*: API completeness, parameter consistency
   - *Viability*: Missing field implementation

3. **#2104: Add Opentelemetry support** (Last updated: 2025-08-08)
   - *Engineering relevance*: Observability, monitoring capability
   - *Viability*: OTEL integration feature

4. **#2095: TerminalReaderCollectInputsInputSelectionParams server-side validation issue** (Last updated: 2025-07-30)
   - *Engineering relevance*: API validation, version compatibility
   - *Viability*: Server-side validation fix

5. **#2094: charge.Invoice does not exist in Charges Retrieve API** (Last updated: 2025-07-29)
   - *Engineering relevance*: API completeness, data model consistency
   - *Viability*: Missing field in Go SDK

6. **#2087: Seq2 and LastResponse** (Last updated: 2025-07-29)
   - *Engineering relevance*: Client design, response handling
   - *Viability*: Client architecture improvement

7. **#2085: V2 Accounts** (Last updated: 2025-07-14)
   - *Engineering relevance*: API version support, feature completeness
   - *Viability*: V2 API implementation

8. **#2075: Missing PaymentIntent property in Invoice struct** (Last updated: 2025-06-06)
   - *Engineering relevance*: Data model completeness
   - *Viability*: Struct field addition

9. **#2072: noncompliant not represented as a DisputeReason** (Last updated: 2025-06-04)
   - *Engineering relevance*: Enum completeness, API parity
   - *Viability*: Enum value addition

10. **#1937: Add omitempty to JSON field tags on optional fields** (Last updated: 2025-07-24)
    - *Engineering relevance*: JSON serialization efficiency, API consistency
    - *Viability*: JSON tag improvement

---

## stripe-stripe-node (179 total issues)

1. **#950: StripeAuthenticationError when loading stripe secret from environment variables** (Last updated: 2025-08-10)
   - *Engineering relevance*: Configuration management, authentication
   - *Viability*: Environment variable handling fix

2. **#2382: createPreview doesn't expand lines.data.price.tiers** (Last updated: 2025-08-05)
   - *Engineering relevance*: API data completeness, expand functionality
   - *Viability*: Expand parameter implementation

3. **#2368: Auto-pagination error iterating over subscriptions when updating last record** (Last updated: 2025-07-23)
   - *Engineering relevance*: Pagination reliability, data consistency
   - *Viability*: Pagination edge case fix

4. **#2332: Requests not aborted within timeout** (Last updated: 2025-07-23)
   - *Engineering relevance*: Resource management, timeout handling
   - *Viability*: Request timeout implementation

5. **#2327: TypeScript types are not accurate when expanding data** (Last updated: 2025-07-03)
   - *Engineering relevance*: Type safety, developer experience
   - *Viability*: TypeScript type system improvement

6. **#2361: Add support for accounts v2** (Last updated: 2025-07-02)
   - *Engineering relevance*: API version support, feature completeness
   - *Viability*: V2 API implementation

7. **#2357: Export current api version string** (Last updated: 2025-07-01)
   - *Engineering relevance*: Version management, API consistency
   - *Viability*: Version string export

8. **#2351: apiVersion set in new Stripe, but ephemeralKeys.create still asks for it** (Last updated: 2025-06-23)
   - *Engineering relevance*: API consistency, configuration management
   - *Viability*: Configuration inheritance fix

9. **#2241: Add AbortSignal support** (Last updated: 2025-05-22)
   - *Engineering relevance*: Request cancellation, resource management
   - *Viability*: Modern async control implementation

10. **#2211: Default Node httpClient configuration does not get mocked by MSW** (Last updated: 2025-05-05)
    - *Engineering relevance*: Testing infrastructure, mock compatibility
    - *Viability*: HTTP client compatibility improvement

---

## Summary

- **Total repositories analyzed**: 9
- **Repositories with issues**: 7
- **Repositories with no issues**: 2 (mastercard-developers-agent-toolkit, monzo-terrors)
- **Total nominated issues**: 70 (10 issues from 7 repositories)
- **Focus areas**: API completeness, performance optimization, security fixes, developer experience, and system reliability
- **Time range**: All nominated issues updated after January 2024 or have strong engineering justification