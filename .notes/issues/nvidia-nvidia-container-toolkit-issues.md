# Issues for NVIDIA/nvidia-container-toolkit

**Total Issues**: 167
**Repository**: https://github.com/NVIDIA/nvidia-container-toolkit

**Open Issues**: 119
**Closed Issues**: 48

---

## Issues List (Most Recently Updated First)

- **#1239: Wrong CDI spec creates error "Unresolvable CDI device"**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-11
  > I am deploying the nvidia gpu operator with RKE2 Kubernetes in a two node clusters, one node having an nvidia GPU. The version of the nvidia-container-toolkit is `v1.17.8`. I am enabling cdi with `cdi...

- **#1186: Docker dropping GPU connection after certain period of time**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-08-09
  > After certain period of time, GPU not detected in container.  For example running nvidia-smi gives: "Failed to initialize NVML: Unknown Error"  This is after the GPU was working successfully in the ru...

- **#564: Fix for "Failed to initialize NVML: Unknown Error"**
  - Labels: question
  - Comments: 4
  - Last updated: 2025-08-09
  > The issue described in https://github.com/NVIDIA/nvidia-container-toolkit/issues/48 which is locked - it states  > A fix will be present in the next patch release of all supported NVIDIA GPU drivers...

- **#1227: Failed to initialize NVML: Unknown Error After "systemctl daemon-reload"**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-08-08
  > ## 1. Summary  On a gpu working node, running `systemctl daemon-reload` cause all running gpu containers to lost gpu devices. ``` (container) $ nvidia-smi -L Failed to initialize NVML: Unknown Error `...

- **#1215: CDI Spec Generation is missing driver libraries**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-08
  > See https://github.com/NVIDIA/k8s-dra-driver-gpu/issues/446 where certain driver libraries are reported as missing when generating CDI specifications. The issue is specifically focussed on a GKE drive...

- **#585: rootless podman sees all GPUs despite cgroups setup**
  - Labels: No labels
  - Comments: 10
  - Last updated: 2025-08-06
  > There is a discussion related to docker #211  But for docker it is expected that root-daemon has access to all gpus.  In my case, I run podman within SLURM, which uses cgroups to control acccess to...

- **#1225: CLI flags should be ignored when an unrecognised hook is detected**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > In #1000 we tried to avoid failures for unsupported hooks (to allow some version skew between toolkit versions). This does not work as expected beacaus the flags passed to the unexepected hook cause a...

- **#1226: Add metadata to generated CDI specs to indicate how the spec was generated**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > Ideally we want to include metadata in the generated CDI spec that includes information on how a specific CDI spec was generated. Using spec-level annotations could make sense, but would generate a `v...

- **#1224: Support IMEX_CHANNELS in `jit-cdi` mode**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-06
  > When using `jit-cdi` mode (the new default in `v1.18.0`) a user requesting imex channels using `IMEX_CHANNELS` should have these injected.

- **#1222: Container Toolkit messed up config.toml in GKE cluster with containerd 2.0**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-05
  > I've been using the GPU Operator to install Nvidia driver in my GKE cluster. This has worked fine until last week when the cluster version is upgraded from GKE 1.32 to 1.33. One of the big change is t...

- **#1218: Disable chmod hook by default**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-08-04
  > The chmod `createContainer` hook was added as a workaround to a specific `crun` issue for device nodes that are found in subdirectories of `/dev`. Since this has since been addressed in `crun`, we sho...

- **#1207: When the prestarthook injected**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-08-04
  > ### command ``` docker run --runtime nvidia --name gpu -itd --gpus all nvidia/cuda:12.6.2-runtime-ubuntu22.04 ```  ### main.go os.Args ``` 1. [nvidia-container-runtime features] 2. [nvidia-container-r...

- **#1208: invalid mitigation of cve-2025-23266**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-08-02
  > In the section Mitigations -> Mitigations for NVIDIA Container Runtime, the instructions state to edit the following file:  > When using the NVIDIA Container Runtime in legacy mode, you can opt out of...

- **#692: libnvidia-egl-wayland.so.1.1.13 not found, podman 5.2.2 update**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-08-02
  > On my Arch Linux system with a 4090, running podman 5.2.2, after doing an update today the following command fails with an error:  ```bash podman run -it -d \     --pod my-own-pod \     --gpus all \...

- **#1209: Multi GPU, NVIDIA_VISIBLE_DEVICES and FFMPEG 7 NVDEC errors**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-08-01
  > So, this is a weird and pretty specific problem. I am at a loss at what I can do next because I am unsure if this is an issue with nvidia or ffmpeg (nvdec specifically). Issue has been observed in the...

- **#1203: CDI behavior with NVIDIA GPU devices in Kubernetes**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-08-01
  > Hello, I'm currently testing the NVIDIA CDI feature.  I've enabled CDI on a host with an NVIDIA GPU, and set ```runtimeClassName: nvidia-cdi``` in my Kubernetes pod spec. Here's what I observed:  ```...

- **#207: The repository 'https://nvidia.github.io/libnvidia-container/stable/ubuntu18.04/amd64  Release' does not have a Release file.**
  - Labels: No labels
  - Comments: 10
  - Last updated: 2025-08-01
  > I am trying to update my Ubuntu 20.04 using sudo apt update and saw the following error messages  ``` E: The repository 'https://nvidia.github.io/libnvidia-container/stable/ubuntu18.04/amd64  Relea...

- **#607: install by apt get Unsupported distribution error.**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-08-01
  > I am following the installation guide to install nvidia-container-toolkit and when I update the apt source I got these error, it seems that the release of ubuntu18.04 doesn't exist anymore. Is there a...

- **#1199: NVIDIA Container Toolkit fails with "libnvidia-ml.so.1 not found" error on RTX 5070 with 570.x drivers**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-07-30
  > NVIDIA Container Toolkit fails with "libnvidia-ml.so.1 not found" error on RTX 5070 with 570.x drivers  Expected vs. Actual Results  Expected Result: "The command should successfully execute and prin...

- **#1210: [Feature Request] Create go benchmarks for the CDI hooks**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-07-30
  > The various CDI hooks of `nvidia-cdi-hook` (create-symlinks, enable-cuda-compat, update-ldcache) are used in NVIDIA DRA driver. Although they are purpose-built and code complexity is pretty low, it is...

- **#1197: Passing individual GPUs to container not working, but passing all is**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-07-28
  > **System**  - Ubuntu server 24.04, fully upgraded. - 2 x V100 GPUs - Driver Version: 570.158.01 - CUDA Version: 12.8  - Docker version 28.3.2, build 578ccf6 - Docker Compose version v2.38.2  **Problem...

- **#1200: does the container toolkit support Debian 12？**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-22
  > I tried so many times， when my input is “sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi”， there is always an error： docker: Error response from daemon: failed to create shim task:...

- **#189: Use cgroup v2 in rootless mode**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-07-22
  > NVIDIA Container Toolkit doesn't work in rootless mode by default, because cgroup is not supported in rootless mode, disabling its use fixed the issue as mentioned in https://github.com/NVIDIA/nvidia-...

- **#1121: Unable to use nvidia container on RTX5090 in ubuntu 22.04**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-07-21
  > # Issue with GPU Access in Docker  After successfully installing Docker and the NVIDIA driver, I ran the following commands to check the installation:  ### NVIDIA Driver Status  ``` ➜  ~ nvidia-smi Sa...

- **#1171: Include Vulkan SC ICDs in containers**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-07-18
  > As of the 560 driver, the NVIDIA driver includes Vulkan ICD files at ``` /usr/share/vulkansc/icd.d/ ``` These should also be detected and included in the same location in the container.

- **#1050: Allow user to opt out of specific CDI hooks**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-07-14
  > When running the `nvidia-ctk cdi generate` command, a user should be able to opt-out of specific hooks. This is important for hooks such as `enable-cuda-compat` which are controlled by feature-flags i...

- **#1027: libnvidia-container1 does not install when you intall the CTK on fedora**
  - Labels: No labels
  - Comments: 11
  - Last updated: 2025-07-13
  > referencing - https://github.com/NVIDIA/nvidia-container-toolkit/issues/1011 Is this a bug that libnvidia-container1 doesnt install when you install the ctk?  The docs says it should be included - htt...

- **#1193: unable to create new device filters program: load program: invalid argument: last insn is not an exit or jmp**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-13
  > Getting ```go docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error runni...

- **#482: Support for Ubuntu 24.04**
  - Labels: No labels
  - Comments: 12
  - Last updated: 2025-07-12
  > Please add support for Ubuntu 24.04.

- **#939: nvidia-ctk doesn't respect spec-dir override**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-07-09
  > $ nvidia-ctk --version NVIDIA Container Toolkit CLI version 1.17.4 commit: 9b69590c7428470a72f2ae05f826412976af1395  $ nvidia-ctk config disable-require = false supported-driver-capabilities = "compat...

- **#1151: use of low level runtime in nvidia-container-runtime**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-07-08
  > I am having an issue with CDI and rootless podman on Ubuntu 24.04.2 LTS when using nvidia-container-runtime. ``` $ nvidia-container-runtime --version NVIDIA Container Runtime version 1.17.8 commit: f2...

- **#1075: Load settings from config.toml file during CDI generation**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-08
  > Most nvidia-ctk commands do not currently load settings from the config.toml file. The one exception is nvidia-ctk config which processes the same config file that the nvidia-container-runtime would....

- **#1163: nvidia-cdi-hook>=1.17.7: Failed to mount /proc in the rootless mode**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-07-07
  > In the rootless (podman) mode, the nvidia-cdi-hook update-ldconfig failed to execute: 1.  The program stucks in `mountProc`, in `internal/ldconfig/ldconfig_linux.go`  ```go // internal/ldconfig/ldconf...

- **#191: loader_scanned_icd_add: Could not get 'vkCreateInstance' via 'vk_icdGetInstanceProcAddr' for ICD libGLX_nvidia.so.0**
  - Labels: No labels
  - Comments: 11
  - Last updated: 2025-07-05
  > hi! I'm trying to use Vulkan in a Docker container. On my host, Vulkan works fine.  I'm using Ubuntu 22.04. I'm using NVIDIA 535.129.03 drivers. I have a Tesla T4 GPU.  I'm using container toolk...

- **#1091: [rpm] libnvidia-container-tools should pin to nvidia-container-toolkit version**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-07-02
  > https://github.com/NVIDIA/nvidia-container-toolkit/blob/ac8f190c991a352733b5f94fc931f350b26756f3/packaging/rpm/SPECS/nvidia-container-toolkit.spec#L24-L25  The latest release of nvidia-container-toolk...

- **#679: docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed.**
  - Labels: No labels
  - Comments: 11
  - Last updated: 2025-07-01
  > ### docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed  **Machine Specs & Environment Setup** OS				: Ubuntu 24.04 LTS NVIDI...

- **#982: container-toolkit does not modify the containerd config correctly when there are multiple instances of the `containerd` binary**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2025-07-01
  > NOTE: This issue is specific to container-toolkit when run as an OCI container via gpu-operator  To enable the nvidia-specific container runtime handlers, the toolkit must overlay config changes on th...

- **#208: Amazon Linux 2023 - driver rpc error: failed to process request: unknown.**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-07-01
  > Trying to run a container using nvidia-container-toolkit fails with the error below when using Amazon Linux 2023. ``` [ssm-user@ip-10-0-0-73 ~]$ sudo docker run --rm --runtime=nvidia --gpus all ubun...

- **#1161: Apt update fails: Release file missing & TLS handshake error due to unresolved $(ARCH)**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-06-28
  > #  Description   Following the official documentation to set up the NVIDIA libnvidia-container APT repository, I encountered a problem:  **`apt update` failed with both a missing Release file and a TL...

- **#1099: Missing libnvidia-ml.so symlinks in containers after host library updates**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2025-06-26
  > ### Summary: After a recent system upgrade on my Arch-based distribution (CachyOS), containers using the NVIDIA container runtime began failing with nvidia-smi due to missing symlinks for libnvidia-ml...

- **#1156: Add ability to remove old configurations to not litter hanging symlinks**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-06-25
  > I use Incus to add a GPU to a container, but doing so creates a symlink over time for each driver version on each upgrade.  These broken symlinks make ldconfig spam every single file each time it is r...

- **#944: LDCache does not include libcuda.so**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-06-24
  > One of the things that the NVIDIA Container Toolkit does is update the ldcache in the container so as to allow applications to discover the host driver libraries that have been injected. We also creat...

- **#1155: GPU in rootless Docker stops working after host is suspended (requires restart)**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-06-24
  > After resuming from suspension, NVIDIA GPU functionality inside rootless Docker containers stops working, even though nvidia-smi runs successfully within the container.  The container can detect and d...

- **#1028: Add envvar to CDI spec that shows libcuda.so.RM_VERSION parent directory in the container**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-06-24
  > It would be useful to include an environment variable (e.g. `LIBCUDA_SO_PARENT_DIRECTORY_CONTAINER_PATH`).

- **#1059: Addressing Security Vulnerability: Red Hat Enterprise Linux 8.6 - python39:3.9 Multiple Vulnerabilities - RHSA-2024:6915**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-06-23
  > # Description 1) The email module didn't properly quote newlines for email headers when serializing an email message allowing for header injection when an email is serialized. [CVE-2024-6923] 2) A reg...

- **#856: nvidia-ctk requires run after kernel/akmod update**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2025-06-22
  > Hello,  When working with podman on fedora and using nvidia GPU using the CDI backend, everytime the kernel is updated or the driver is updated, `nvidia-ctk cdi generate ...` to be required to be re-r...

- **#126: Using `docker-compose` and cdi to passthrough gpu to container via `podman`**
  - Labels: No labels
  - Comments: 9
  - Last updated: 2025-06-22
  > # Running `docker` and `podman` directly  Works: * `sudo docker run --rm --device nvidia.com/gpu=all ubuntu nvidia-smi -L` * `sudo podman run --rm --device nvidia.com/gpu=all ubuntu nvidia-smi -L`...

- **#848: Help Needed: NVIDIA Docker Error - libnvidia-ml.so.1 Not Found in Container**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-06-21
  > Hi everyone, I’ve been struggling with an issue while trying to run Docker containers with GPU support on my Ubuntu 24.04 system. Despite following all the recommended steps, I keep encountering the f...

- **#305: Error occuring in release 1.14.4: load library failed: libnvidia-ml.so.1: cannot open shared object file**
  - Labels: No labels
  - Comments: 18
  - Last updated: 2025-06-18
  > Hello, I'm getting a load library failed error as as previous issue (unsure whether related, hence the new issue) when running a nextflow pipeline with docker that uses the nvidia-runtime-toolkit. It...

- **#1042: Addressing Security Vulnerability: Go 1.23.x < 1.23.8 - HTTP Request Smuggling Vulnerability - 1.23.8**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-06-18
  > # Description net/http: request smuggling through invalid chunked data: The net/http package accepts data in the chunked transfer encoding containing an invalid chunk-size line terminated by a bare LF...

- **#1049: Gated modifiers ignore device requests by volume mounts**
  - Labels: bug
  - Comments: 0
  - Last updated: 2025-06-17
  > The gated modifiers used to add support for GDS, Mofed, and CUDA Forward Comatibility only check the `NVIDIA_VISIBLE_DEVICES` envvar to determine whether GPUs are requested and modifications should be...

- **#1138: container run failed when using containerd instead of docker**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-06-16
  > **1. Issue or feature description** ctr run --rm -t   --gpus 0 general-vllm-infer-service:0.1.8 test nvidia-smi  ctr: failed to create shim task: OCI runtime create failed: runc create failed: unable...

- **#1037: How to change the jupyter lab host in Pytorch image**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-06-14
  > After downloading the 25.03-py3 and trying to run Jupyter in VS Code in my container, I ran across the issue described in https://github.com/NVIDIA/nvidia-docker/issues/1774, which was closed with the...

- **#1142: Generic installation instructions fail for ubuntu 24.04**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-06-13
  > I did the following  1) curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \   && curl -s -L https://nvidia...

- **#846: RTX4090 - Fedora 41 (LLM AI) Unable to determine the device handle for GPU0000:01:00.0: Unknown Error**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-06-09
  > hi Team , I am having an issue with RTX4090 and Fedora41. It was working fine since implementation until during an embedding model work for document inference from a container(running in gpu), went in...

- **#1124: vulkan failed in RHEL8(`vkCreateInstance failed with ERROR_INCOMPATIBLE_DRIVER`)**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2025-06-05
  > When I tried vulkaninfo in RHEL8,  it failed.  ``` $ docker run --runtime=nvidia --gpus all -it --rm  nvcr.io/nvidia/clara-holoscan/holoscan:v3.2.0-dgpu /bin/bash root@a26235e4fd7f:/opt/nvidia/holosca...

- **#48: NOTICE: Containers losing access to GPUs with error: "Failed to initialize NVML: Unknown Error"**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-06-05
  > ## 1. **Executive summary**  Under specific conditions, it’s possible that containers may be abruptly detached from the GPUs they were initially connected to. We have determined the root cause of th...

- **#1047: how to get Vulkan working on Docker swarm**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-06-05
  > I am trying to deploy docker swarm stack with an app that needs GPU Vulkan acceleration. It works in standalone docker when I run it like this: ``` $ docker run --rm \     --gpus all \     -e NVIDIA_D...

- **#1093: Update to version 1.17.7-1 on Ubuntu breaks pyxis/enroot in Slurm**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2025-06-05
  > As reported in this enroot issue https://github.com/NVIDIA/enroot/issues/232, the 1.17.7-1 version of the container toolkit breaks the use of enroot containers with slurm. Downgrading to a previous to...

- **#1101: Update to version 1.17.7-1 on archlinux leads to segfault on container startup**
  - Labels: No labels
  - Comments: 20
  - Last updated: 2025-06-05
  > **Problem:** All the containers that utilize the `nvidia-container-toolkit` docker runtime hang in *Created* state. Nothing suspicious in the `nvidia-container-toolkit`, but segfaults in `dmesg` outpu...

- **#1074: Add a flag to nvidia-ctk cdi generate to allow users to specificy which Hooks to be skipped**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-06-03
  > When running the `nvidia-ctk cdi generate` command, a user should be able to opt out of specific hooks.  We propose to add a flag `--skip-hooks` that will take a comma-separated list of hooks that wil...

- **#767: The NVIDIA ICD JSON occasionally goes missing from 'nvidia-ctk cdi generate'**
  - Labels: No labels
  - Comments: 10
  - Last updated: 2025-06-02
  > I have been playing with the NVIDIA Container Toolkit on Fedora 39 Workstation and the proprietary NVIDIA driver from RPM Fusion.  I have noticed that the NVIDIA installable client driver (or ICD) JSO...

- **#1116: Seeking ContainerOS-friendly Driver Deployment with CDI Path Consistency**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-06-01
  > Hi,  We're implementing GPU support on ContainerOS-based Kubernetes nodes with two critical requirements:  1. **Security-driven path isolation**: All driver files (.so, bins, configs) must reside unde...

- **#1109: Update libnvidia-container to v1.17.8**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-05-28
  > https://github.com/NVIDIA/libnvidia-container/milestone/4

- **#236: driver rpc error: failed to process request: unknown.**
  - Labels: No labels
  - Comments: 24
  - Last updated: 2025-05-27
  > ### 1. Issue or feature description  Hello!  I get an error when I start the container:  ``` docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc crea...

- **#216: `nvidia-smi` shows different CUDA versions inside and outside Docker**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-05-23
  > _The template below is mostly useful for bug reports and support questions. Feel free to remove anything which doesn't apply to you and add more information where it makes sense._  _Also, before rep...

- **#1089: NVIDIA Container Runtime Not Functioning Correctly in RKE2 (Missing Devices/Libraries)**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2025-05-22
  > ### Desired goal Spin up a rke2 cluster with the ability to deploy GPU enabled pods via ```runtimeClassName: nvidia``` ### Issues I've observed  After I create a pod with a pod spec of  ```yaml cat <<...

- **#1094: nvidia-ctk cdi generate output is not deterministic**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-05-22
  > After multiple runs of `nvidia-ctk cdi generate` the mount list has different order  ```bash diff run2 run1 26,27d25 <     - libGLX_nvidia.so.575.51.03::/usr/lib/x86_64-linux-gnu/libGLX_indirect.so.0...

- **#1098: CDI Implementation with Kubernetes and Containerd with CRIU**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-05-22
  > Hello team, good day. I am currently testing to run CRUI with Kubernetes/Containerd with GPU-Operator. I am currently leaning on testing CDI implementation with CRIU. During my tests, I encountered so...

- **#116: RHEL rpm package transaction test failure with FIPS mode **
  - Labels: No labels
  - Comments: 18
  - Last updated: 2025-05-19
  > ## Platform Information - FIPS mode enabled machine  ```bash ARCH=x86_64 NAME="Red Hat Enterprise Linux" VERSION="8.8 (Ootpa)" ID="rhel" ID_LIKE="fedora" VERSION_ID="8.8" PLATFORM_ID="platfo...

- **#85: Can rootless and rooted both docker use GPU without changing no-cgroups?**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2025-05-19
  > ### 1. Issue or feature description  Both rootless and rooted docker can't seem to access GPU without setting a config in `/etc/nvidia-container-runtime/config.toml`.   The setting needs to be mod...

- **#1092: Current instructions don't work for installation.**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-18
  > Working from a fresh Ubuntu 24.04 install, I can't get nvidia-container-toolkit working.  I've tried a bunch of times, no matter what I follow I get: ``` Error response from daemon: failed to create t...

- **#1084: What's the relationship between NVIDIA Container Toolkit and the nvidia/cuda docker image?**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-05-16
  > We are building a service that utilizes CUDA, and would like to run it in a container. However we are getting confused on how to have proper CUDA support in the container: 1) do we have to use the `nv...

- **#1088: /usr/local/cuda symlink broken in nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-16
  > The official CUDA base image nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04 has a broken symlink:  /usr/local/cuda -> /tmp/tmpayalvm_3m/cuda-11  However, the target /tmp/tmpayalvm_3m/cuda-11 does not exi...

- **#957: hi**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-16
  > rtx 5090 rtx 5090 Error creating song: CUDA error: no kernel image is available for execution on the device Compile with TORCH_USE_CUDA_DSA to enable device-side assertions. how i can fix

- **#1057: Security concern**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-16
  > Hello 👋  I run a security community that finds and fixes vulnerabilities in OSS. A researcher (@michaelpierre) has found a potential issue, which I would be eager to share with you.  Could you add a `...

- **#248: Feature request: use GPU if available, else start container without one**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-15
  > I'm using `docker compose` to run a container:  ``` version: "3.9" services:   app:     image: nvidia/cuda:11.0.3-base-ubuntu20.04     deploy:       resources:         reservations:...

- **#1067: Use drop-ins for containerd configuration when available**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-05-12
  > As of v2.0.0 and config version 3, containerd supports a more advanced merge strategy for configuration that would allow the NVIDIA runtimes to be configured in their own file.  This avoids the need t...

- **#1045: Generate CDI specifications for architectures other than x86_64**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-09
  > The `nvidia-ctk` helper program fails to parse the `ldcache` file for `aarch64` because the list of flags in the code that parses this file is incomplete, compared to its [counterpart] in `libnvidia-c...

- **#1051: Error running NVIDIA Container with Docker on Ubuntu 22.04**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-06
  > Hi ,  I installed a new Ubuntu 22.04 Ubuntu machine and performed following actions.  1. Installed GPU Driver as per the instruction here : https://docs.nvidia.com/datacenter/tesla/driver-installation...

- **#1060: nvidia-container-toolkit**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-05-06
  > [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)  支持Centos7

- **#1054: Sharing one GPU among many containers**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-28
  > Is there an option in "nvidia-ctk config" to set a limit on for how long a container can hold on to the GPU. Currently, it looks like once a container has grabbed the GPU (Memory), it can hold onto it...

- **#1053: nvidia-smi hangs in container when running with nvidia-persistenced**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-28
  > When enabling `nvidia-persistencd` service on the host running `nvidia-smi` in a container takes much longer (2s vs. 24s) than without. I did some investigation using `strace` and it seems like the co...

- **#1041: Vulkan Cannot Access GPU Inside Docker After Upgrading Driver to 570 from 550**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-04-27
  > After upgrading my Nvidia driver from 550 to 570, Vulkan is no longer able to access GPU(s) inside a Docker container.  **System Information**  My machine is running Ubuntu 22.04.5 LTS.  ```Bash nvidi...

- **#918: Screen Tearing in games (run using wine/lutis/steam) with Nvidia RTX 4090 and docker-nvidia-egl-desktop**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-04-25
  > I am using docker-nvidia-egl-desktop to launch containers on a headless server having NVIDIA RTX 4090 card , and streaming using webrtc . When I launch games using wine/lutris/steam ,with Xvfb resolut...

- **#1013: Unable to see gpu processes pid inside the container**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-04-23
  > When I run any gpu process inside my rootful podman container, I see that GPU is getting utilised but the pids are not visible in the output of `nvidia-smi`  **Steps to reproduce the issue**  1. `sudo...

- **#1036: Rootless Docker / Ubuntu 24.04.2 (6.8.0-58-generic) / Latest nvidia-container-toolkit**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-04-21
  > I have setup docker rootless by following these two guides:  https://docs.docker.com/engine/security/rootless/ https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload....

- **#1034: nvidia-container-cli: mount error: mount operation failed: /home/cgy/docker/vfs/dir/4136651d020cab1c7290caefe7c69f4e233a6364f2ebae5694412f8f24359ea7/proc/driver/nvidia: permission denied:**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-04-21
  > cgy@cgy2:~$ sudo docker run --privileged=true  -v /home/cgy/sys/fs/vfs:/sys/fs/cgroup --rm --gpus all nvidia/cuda:12.1.1-base-ubuntu22.04 nvidia-smi  docker: Error response from daemon: failed to crea...

- **#381: Failed to initialize NVML: Unknown Error - Even after reading the pinned issue**
  - Labels: No labels
  - Comments: 27
  - Last updated: 2025-04-21
  > Hi,   I'm trying to understand what I might be missing with my devbox which suddenly loose access to GPUs with Docker with the above message **"Failed to initialize NVML: Unknown Error"**.  I spot...

- **#1040: Container Toolkit shutdown config.toml modification**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-18
  > When the Nvidia’s Container Toolkit pod shuts down, it update the containerd’s config.toml file in such a way that etcd and API Service pods crash after a reboot. Here are details based on my observat...

- **#1038: nvidia-container-cli: mount error: mount operation failed: permission denied by docker/vfs/dir/**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-18
  > cgy@cgy2:~$ docker run -v /home/cgy:/sys/fs/cgroup --gpus all ubuntu:20.04  nvidia-smi docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime...

- **#1021: Vulkan run with cpu instead of GPU in docker with cuda 12.8**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-04-15
  > As the title suggests, I am trying to run Vulkan on a GPU inside a Linux Docker container. I am using nvidia/cuda:12.8.0-cudnn-devel-ubuntu24.04.  On my host machine, everything works fine, and when I...

- **#1032: nvidia-container-runtime update oci spec when container set NVIDIA_VISIBLE_DEVICES=all**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-15
  > ### Problem Description:   We are using the k8s device plugin deployed via DaemonSet (https://github.com/NVIDIA/k8s-device-plugin/tree/main/deployments/helm). For security purposes, we did **not** se...

- **#1031: GitHub Issue: GPU Integration in k3s Using nvidia-open Drivers on RTX 5080 (Containerd + No Proprietary Runtime)**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-15
  > 🧩 Summary I'm running a single-node k3s cluster on a workstation with an NVIDIA RTX 5080 GPU using open-source drivers (nvidia-open) on Arch Linux. I want to run vLLM, Whisper, and other CUDA-dependen...

- **#883: the instructions caused my installation to be downgraded.**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-04-12
  > ![Image](https://github.com/user-attachments/assets/b76bfc9c-9b19-4810-bbf8-e78782004c64)  i can see that the version in the document latest is shown as 1.17.3   is there a reason why following the in...

- **#871: docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-04-10
  > I followed all the steps for installing the toolkit and docker, I also tried working with /etc/nvidia-container-runtime/config.toml, but this problem persists:  ![Image](https://github.com/user-attach...

- **#803: container-toolkit on k0s leads to unsupported config version: 3**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2025-04-08
  > Hello,  I'm trying to install nvidia helm in a k0s cluster:  ``` [root@miriam ~]# k0s version v1.31.2+k0s.0 [root@miriam ~]# /var/lib/k0s/bin/containerd -v containerd github.com/containerd/containerd...

- **#1011: Getting the famous error after following the nvidia-container-toolkit docs**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-04-08
  > docker run --rm --gpus all ubuntu:latest nvidia-smi docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]]  Run 'docker run --help' for more information  Syst...

- **#1010: can't launch any containers with GPU passed through - 5070 TI or driver issue?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-04-05
  > As the title says, I can't even launch the sample workload:  ``` ❯ sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi docker: Error response from daemon: failed to create task for cont...

- **#1018: Can't select candidate version from package libnvidia-container-tools as it has no candidate**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-04-03
  > OS: Ubuntu 22.04  sourcelist:  deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://nvidia.github.io/libnvidia-container/stable/ubuntu22.04/$(ARCH) / deb [signed-by=/usr/sh...

- **#731: The mounts discoverer cache usage is racey**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-04-02
  > The mount cache is read here without locking: https://github.com/NVIDIA/nvidia-container-toolkit/blob/4604e3b6c86aba52c7fe54241070d493938a28e6/internal/discover/mounts.go#L59-L67  But it is set here w...

- **#934: intended behavior for >=1.17.4 for distributed training workloads with CVE fixes?**
  - Labels: No labels
  - Comments: 9
  - Last updated: 2025-03-31
  > I/my team were impacted by the changed from https://github.com/NVIDIA/nvidia-container-toolkit/pull/877 after upgrading to 1.17.4 while maintaining security SLAs for https://nvd.nist.gov/vuln/detail/C...

- **#672: nvidia-smi is not mounted into container**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-03-25
  > I am using the VM (Debian 12) in the GCP Cloud with GPU attached.  ``` gfrankliu-t4-ws ➜  ~ export PATH=/var/lib/nvidia/bin:$PATH gfrankliu-t4-ws ➜  ~ export LD_LIBRARY_PATH=/var/lib/nvidia/lib64 gfra...

- **#572: where is the docs of /etc/nvidia-container-runtime/config.toml?**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2025-03-24
  > where is the docs of /etc/nvidia-container-runtime/config.toml?   thanks so much.

- **#394: nvidia-container-cli: initialization error: nvml error: driver/library version mismatch: unknown.**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-03-23
  > Hi everyone,   I've been following the instruction of installation Alphafold2 and I was able to run the command in step 4 with docker image of ubuntu 22.04, and get a correct information chart. Howe...

- **#930: load library failed: libnvidia-ml.so.1: opensuse tumbleweed**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-03-21
  > Error on fresh opensuse tumbleweed install   Error message when running a test docker container. `dan@localhost:~> docker run --gpus all hello-world docker: Error response from daemon: failed to creat...

- **#994: nvidia-container-toolkit/runtime repository for Ubuntu 24.04 (Noble)**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-03-20
  > Hi,   I would like to know when the repository for Ubuntu 24.04 will be available ?  https://nvidia.github.io/nvidia-container-runtime/

- **#942: Does CDI mode support CUDA Forward Compatibility?**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-03-18
  > hi, I was reviewing the [CVE-2025-23359 security bulletin](https://nvidia.custhelp.com/app/answers/detail/a_id/5616/~/security-bulletin%3A-nvidia-container-toolkit---11-february-2025) and noticed that...

- **#996: libcontainer execseal Import Incorrect v1.17.5**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-03-17
  > The new libcontainer execseal implementation is using the old name, `libcontainer/dmz`. This has been migrated to `libcontainer/execseal`.   https://github.com/NVIDIA/nvidia-container-toolkit/commit/5...

- **#995: bumping tags.cncf.io/container-device-interface from v0.8.0 to v1.0.0 downgrade go version of nvidia-container-toolkit**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-03-17
  > As part of a version bump in our project (https://github.com/canonical/lxd) from `tags.cncf.io/container-device-interface v0.8.0` to `tags.cncf.io/container-device-interface v1.0.0` , we also had to u...

- **#908: docker  stderr: nvidia-container-cli: initialization error: cuda error: os call failed or operation not supported on this os: unknown.**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-03-14
  > I use the docker run - gpus all - d - v/opt/ai/ollama: / root/ollama -p 11434:11434 - name ollama ollama/ollama 'docker to run this command The image file in is incorrectly displayed  Error content  '...

- **#988: Customizing the docker container**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-03-14
  > Hello there,  Excuse my complete ignorance. I'm quite new to the current NVIDIA containers.  I need to deposit my own scripts inside a cuda-enabled container, meaning a dedicated conda environment, ma...

- **#983: Unable to limit container to see just a single GPU device**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-03-12
  > `docker run --runtime=nvidia --gpus '"device=1"' -e NVIDIA_VISIBLE_DEVICES=1 -e CUDA_VISIBLE_DEVICES=1 nvidia/cuda:12.8.0-base-ubi9 nvidia-smi -L`  Returns multiple GPUs, instead of just GPU 1  - WSL...

- **#832: MIG support for HPL benchmark**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-03-11
  > Hi,  I'm trying to run the NVIDIA HPL benchmark with the NVIDIA container toolkit as described [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/hpc-benchmarks). The only difference is that...

- **#217: failed to start daemon: Error initializing network controller: error obtaining controller instance: failed to create NAT chain DOCKER: iptables failed: iptables -t nat -N DOCKER: iptables v1.8.4 (legacy): can't initialize iptables table `nat': Permission denied (you must be root)**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-03-11
  > Hello to everyone.  This is the continuation of this post : https://github.com/NVIDIA/nvidia-container-toolkit/issues/137  Yesterday I have installed ubuntu 20.04 within one lxc container (lxc ins...

- **#972: sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml   with errors**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-03-08
  > i run this    sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml  then two files not found   pattern libnvidia-sandboxutils.so.1 not found Could not locate libnvdxgdmal.so.1: pattern libnvdxgd...

- **#854: docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-03-08
  > I have docker and nvidia-container-toolkit installed on my system (Ubuntu 24.04) but I keep getting the error on the title when I try to run any image that needs access to gpu.  Here are some more det...

- **#580: Insufficient permissions error for non-root container user using Podman v5 **
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-03-07
  > The following command   ``` podman run --rm --device nvidia.com/gpu=all -it -u 1000 ubuntu nvidia-smi -L ```  fails on OpenSUSE Tumbleweed (podman 5.1.1) with the error  ``` Failed to initial...

- **#681: cri-o fails to start after nvidia-ctk runtime configure: conmon executable file not found in $PATH**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-03-06
  > I performed the setup in a `cri-o` environment based on the document below, but afterward, `cri-o` started failing to launch.  https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/...

- **#218: nvidia-smi failed to solve error when running a simple docker build **
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-03-05
  > ### 1. Issue or feature description  Getting the following error when running a docker build.  `ERROR: failed to solve: process "/bin/sh -c nvidia-smi" did not complete successfully: exit code: 12...

- **#774: DEB822-STYLE format for Ubuntu 24.04+ apt repository instructions (.sources)**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-03-04
  > Ubuntu from 24.04 is now migrating to defaulting to the use of [DEB822-STYLE sources.list.d](https://repolib.readthedocs.io/en/latest/deb822-format.html) format files, in particularly when you use `ad...

- **#688: Linux Apt Key for nvidia.github.io/libnvidia-container is Failing Due to GitHub CLI Apt Key Update**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2025-03-02
  > When running `$ sudo apt-get update -y` in `Ubuntu 20.04.6 LTS`, the following errors are seen -  ``` Get:2 https://nvidia.github.io/libnvidia-container/stable/ubuntu18.04/amd64  InRelease [1484 B] .....

- **#128: request: Option for nvidia-ctk cdi generate to also create .so.1 files.**
  - Labels: No labels
  - Comments: 16
  - Last updated: 2025-03-01
  > Hi there,  I'm running emby media server with podman on Fedora 39. I'm generating the cdi file with: ```nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml``` Which seems to work just fine.  H...

- **#946: NVIDIA GPU Detected on Host but Not Working in Docker Containers: "NVIDIA Driver was not detected"**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-02-27
  > Hello,  I'm experiencing an issue with NVIDIA GPU passthrough to Docker containers. While my GPU works perfectly on the host system, Docker containers cannot properly access it despite having the NVID...

- **#940: Does cuda container support backwards compatibility?**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-02-26
  > From cuda compatibility [doc](https://docs.nvidia.com/deploy/cuda-compatibility/), newer cuda runtime could run on older cuda driver.  But that doesn't hold with cuda container. I tried ```shell docke...

- **#56: Overriding nvidia-container-runtime/config.toml with XDG_CONFIG_HOME**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-02-23
  > Per documentation:  > The NVIDIA Container Runtime uses file-based configuration, with the config stored in /etc/nvidia-container-runtime/config.toml. The /etc path can be overridden using the XDG_C...

- **#932: Containerd pods logging "Failed to initialize NVML: Unknown Error"**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-02-19
  > Hi, after switching over to the systemd driver after migrating to cgroupv2 (over cgroupfs) for both containerd + kubelet, we noticed pods which are calling `nvidia-smi` began failing with `"Failed to...

- **#931: Doesn't work with OpenGL ES**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-02-19
  > From here on I will talk about how I tried to run in two containers: Ubuntu 22.04 and Ubuntu 24.04. ~~~bash IMAGE=ubuntu:24.04 #IMAGE=ubuntu:22.04 docker run -it --name dev_test  -u root --net host --...

- **#68: OCI runtime create failed**
  - Labels: No labels
  - Comments: 7
  - Last updated: 2025-02-17
  > ```log docker: Error response from daemon: failed to create shim task: OCI runtime create failed: unable to retrieve OCI runtime error (open /run/containerd/io.containerd.runtime.v2.task/moby/665f824...

- **#929: GPU not detected inside container (NVML "Driver/library version mismatch" error)**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-02-16
  > Hello,    I am facing an issue where my **host machine detects the GPU correctly**, but inside the **Docker container**, I get the following error when running `nvidia-smi`:    ``` Failed to initializ...

- **#916: Does it need to be installed somewhere ?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-02-10
  > I apologize for certainly missing the obvious. I guess this is clear for most people, otherwise this would have been clarified.  I just discovered the nvidia-container-toolkit.  The git readme indicat...

- **#674: Save (Win11) & Load (Ubuntu) Leading to "NVIDIA-SMI couldn't find libnvidia-ml.so library in your system"**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-02-10
  > ### Machines:  1. Windows 11 Laptop, Docker Desktop with nvidia-container-toolkit and WSL2 back-end.  2. Remote server, running Ubuntu 20.04.6 LTS, docker with nvidia-container-toolkit installed.   Bo...

- **#811: nvidia-container-toolkit fails to create /etc/vulkan/icd.d/nvidia_icd.json**
  - Labels: No labels
  - Comments: 6
  - Last updated: 2025-02-08
  > When installing using toolbox on Fedora Silverblue 41, the nvidia-container-toolkit doesn't create the file /etc/vulkan/icd.d/nvidia_icd.json necessary for Vulkan to operate correctly--it doesn't find...

- **#154: nvidia-container-cli: initialization error: load library failed: libnvidia-ml.so.1**
  - Labels: No labels
  - Comments: 49
  - Last updated: 2025-02-06
  > Hello,  I tried the different combinations of conda and pip packages that people suggest to get tensorflow running for the rtx 30 series.  Thought it was working after utilizing the gpu with keras t...

- **#196: Docker fails to recognize Nvidia runtime without sudo**
  - Labels: No labels
  - Comments: 5
  - Last updated: 2025-02-04
  > ### 1. Issue or feature description I am trying to run a Docker container which utilizes my Nvidia GPU. I installed Docker via https://docs.docker.com/engine/install/ubuntu/, setup rootless permissio...

- **#797: Parsing default IMEX info fails for legacy images**
  - Labels: bug
  - Comments: 8
  - Last updated: 2025-02-04
  > Since the latest 1.17.x versions, containers with images considered "legacy" and that do not have the `NVIDIA_IMEX_CHANNELS` environment variable set fail to start with the following error:  ``` Error...

- **#145: sudo yum install -y nvidia-container-toolkit failed - No such device**
  - Labels: No labels
  - Comments: 8
  - Last updated: 2025-02-03
  > I am using AWS EC2(Tesla T4) , I think nvidia diver has been installed by default.  Run nvidia-smi get proper outputs.  Thu Nov  9 07:36:11 2023        +------------------------------------------...

- **#833: How to expose the GPU through the (podman) api**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-02-03
  > Hi all, I have been failing to figure out how to properly "translate" the direct container creation with podman to its API equivalent, in particular the: "--device nvidia.com/gpu=all"  part. I have tr...

- **#888: nvidia-container-toolkit**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-02-03

- **#229: Docker Desktop and Nvidia Runtime inoperable across multiple distros**
  - Labels: No labels
  - Comments: 12
  - Last updated: 2025-02-02
  > ### 1. Issue or feature description  On fresh Arch (EndeavourOS) and Ubuntu (20.04 and 22.04) installations, attempts to utilize nvidia runtime through any image via Docker Desktop fail with this er...

- **#886: [release-1.17] Minimum required Go version in go.mod is 1.20, which isn't enough**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-01-30
  > Commits [fa5a4ac499d7327b](https://github.com/NVIDIA/nvidia-container-toolkit/commit/fa5a4ac499d7327b5b7e9c5b3b8984ac143346fe) and [aa946f3f59c82c58](https://github.com/NVIDIA/nvidia-container-toolkit...

- **#885: Rootless Podman Error: setting up CDI devices: failed to inject devices: failed to stat CDI host device "/dev/dri/renderD129": no such file or directory**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-01-30
  > Had installed nvidia-container-toolkit in ubuntu 22.04 container using distrobox ( podman ). But when I tried to enter the distrobox, below was the error I received.   ``` distrobox enter ubuntu  Erro...

- **#884: NVIDIA_VISIBLE_DEVICES in my docker images no longer respected**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-01-30
  > I'm running a server with two A6000 GPUs, a jupyterhub with dockerspawner and a list of docker images, some of them are supposed to have GPU support and some are not. To achieve this, I configured the...

- **#837: nvidia-container-toolkit repo unable to download**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-01-30
  > Why am I unable to download the nvidia container toolkit repo?   dnf config-manager --add-repo https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo Updating Subscripti...

- **#105: Error response from daemon: failed to create shim task: OCI runtime create failed:**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2025-01-29
  > I use the same command "docker run --gpus all sentinel-final:2.1" to run it and it runs fine. But after a few runs it gives the following error. I had to reinstall docker to get this fixed. My docker...

- **#857: docker: Containers losing access to GPUs with error: "Failed to initialize NVML: Unknown Error"**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2025-01-17
  > Running standalone docker container in an Azure Linux 2.0 VM with nvidia container toolkit installed will lose access to the GPU and throw the error: "Failed to initialize NVML: Unknown Error" after t...

- **#842: nvmlDeviceGetMemoryInfo, Insufficient Permissions**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2025-01-16
  > The running container uses the MIG device. Use the API to obtain MemoryInfo in the container. Sample code: ``` >>>import pynvml >>> pynvml.nvmlInit() >>> handle = pynvml.nvmlDeviceGetHandleByIndex(0)...

- **#603: How to install NVIDIA Container toolkit**
  - Labels: No labels
  - Comments: 25
  - Last updated: 2025-01-16
  > Hello,Everyone:   I have a problem that I encountered while using the [NVIDIA Container Toolkit guid](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#insta...

- **#795: NVIDIA_DRIVER_CAPABILITIES=graphics is broken on Jetson devices (1.17.1 or later)**
  - Labels: bug
  - Comments: 7
  - Last updated: 2025-01-14
  > ## Summary  On Jetson(`aarch64`, `Tegra SoC`) devices, version `1.17.1` is not creating containers properly, if environment variable `NVIDIA_DRIVER_CAPABILITIES` contains any of `display`,`graphics`,`...

- **#859: Cuda Toolkit Docker**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-01-14

- **#834: Can not checkpoint container created with nvidia-container-runtime (mounted gpu)**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2025-01-03
  > It's an issue raised by @gflarity in https://github.com/opencontainers/runc/issues/4522  I wonder if docker checkpoint(CRIU) can work with the GPU container created by nvidia-container-runtime. It see...

- **#841: nvidia-cdi-hook fails to execute properly in NixOS (Possibly related to dynamic linking and glibc conflicts)**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2025-01-01
  > I'm not fully sure I understand why (although this issue in nixpkgs might be related https://github.com/NixOS/nixpkgs/issues/338511)  but the nvidia-cdi-hook commands generated by calling cdi generate...

- **#840: After setup config to crio, crio can not stop container anymore.**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2024-12-31
  > Hello there, I found a Fatal Error in nvidia-ctk. After run the config command as **```README```** says: ``` nvidia-ctk runtime configure --runtime=crio --set-as-default --config=/etc/crio/crio.conf.d...

- **#836: How to configure nvidia-container-runtime to expose only certain GPUs from the host to docker**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-12-30
  > Hi there,  In our use case, we have 1 k8s node (special-designed hardware) with 3 GPUs, 2 GPUs used for container workloads and 1 GPU used for display purposes. In the current setup, all three GPUs ar...

- **#754: "Version Not Supported" for Ubuntu Server 24.04.1 LTS**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2024-12-29
  > I am trying to install nvidia-container-toolkit for my headless version of Ubuntu, specifically the Ubuntu Server OS. Ubuntu claims that the current version of the nvidia-container-toolkit does not su...

- **#814: Is Ubuntu 24.04.1 supported now?**
  - Labels: No labels
  - Comments: 3
  - Last updated: 2024-12-26
  > I have a container ran well. Later I got this error docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].  docker --version Docker version 27.3.1, build ce1...

- **#510: Cannot run `hello-world` from NixOS**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-12-23
  > I currently have:  ``` ❯ sudo docker run --rm --gpus all hello-world docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed:...

- **#839: Segmentation fault after installing nvidia-container-toolkit via yum**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2024-12-19
  > I installed the package using  sudo yum install -y nvidia-container-toolkit  The installation looks fine with the following output:  > Running transaction check Running transaction test Transaction te...

- **#817: Failed to initialize NVML: Unknown Error**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-12-17
  > **Here is my operating procedure** ![Image](https://github.com/user-attachments/assets/383f9538-5340-4f47-b607-e72dd15c84d2) ![Image](https://github.com/user-attachments/assets/961da7b5-e0ea-4af5-9685...

- **#714: How to use MPS to share GPUs in multiple Docker containers?**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-12-16
  > os: `redhat7.9` docker version: `20.10.21` nvidia-container-runtime: `3.13.0-1` nvidia-container-toolkit: `1.13.5-1`  I performed the following steps: 1. Open MPS on the physical machine. `nvidia-cuda...

- **#277: Volta MPS Server error "Receive command failed, assuming client exit. Client process disconnected"**
  - Labels: No labels
  - Comments: 4
  - Last updated: 2024-12-13
  > I'm using [aws-virtual-gpu-device-plugin](https://github.com/awslabs/aws-virtual-gpu-device-plugin) which is a solution built on top of Multi-Process Service(MPS) to expose arbitrary number of virtual...

- **#831: Process hang in docker when deploying MPS in host.**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-12-12
  > I have deployed MPS in host.  ``` nvidia-cuda-mps-control -d ``` When running `docker run` command, the container hang. ``` docker run --gpus device=0 --ipc=host -u 1000:1000 --name test -it --rm e265...

- **#689: Understanding of how OpenGL libraries are linked to an application within a container**
  - Labels: question
  - Comments: 1
  - Last updated: 2024-12-11
  > Hello,  This is not a bug, just a question to understand what I am doing.  I use the GPU operator to deploy OpenGL applications in a Kubernetes Cluster. It works fine, my pod (a basic glxgears) starts...

- **#830: Attempting to run nvidia-container-runtime returns  nvidia-container-cli.ldconfig value "/usr/sbin/ldconfig" is not host-relative (does not start with a '@') error**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2024-12-11
  > As the title says, when trying to run the nvidia-container-runtime, the command will return the following error:  `ERRO[0000] error loading config: nvidia-container-cli.ldconfig value "/usr/sbin/ldcon...

- **#829: Multi -graphics card utilization problem**
  - Labels: No labels
  - Comments: 0
  - Last updated: 2024-12-09
  > When I run my computing program through Docker, only one graphics card's video memory is completely occupied, and other graphics cards do not work. How should I use all my graphics cards? Mon Dec  9 1...

- **#815: Cannot download https://nvidia.github.io/libnvidia-container/gpgkey on test machine**
  - Labels: No labels
  - Comments: 2
  - Last updated: 2024-12-05
  > Hi nvidia-container-toolkit team, I got problem when I tried to download https://nvidia.github.io/libnvidia-container/gpgkey with command $ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgk...

- **#819: Support For CUDA 8.0**
  - Labels: No labels
  - Comments: 1
  - Last updated: 2024-12-05
  > I have a very old GPU (GeForce 710M) and therefore am stuck with Ubuntu 16.04 + CUDA 8.0. I've learned that I need to install the deprecated Nvidia Docker 2 instead of Nvidia Container Toolkit. I've t...

