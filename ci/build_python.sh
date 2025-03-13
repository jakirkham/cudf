#!/bin/bash
# Copyright (c) 2022-2025, NVIDIA CORPORATION.

set -euo pipefail

source rapids-configure-sccache

source rapids-date-string

export CMAKE_GENERATOR=Ninja

rapids-print-env

rapids-generate-version > ./VERSION

rapids-logger "Begin py build"

CPP_CHANNEL=$(rapids-download-conda-from-s3 cpp)

RAPIDS_PACKAGE_VERSION=$(head -1 ./VERSION)
export RAPIDS_PACKAGE_VERSION

# populates `RATTLER_CHANNELS` array
source rapids-rattler-channel-string

source ./ci/use_conda_packages_from_prs.sh

rapids-logger "Prepending channel ${CPP_CHANNEL} to RATTLER_CHANNELS"

RATTLER_CHANNELS=("--channel" "${CPP_CHANNEL}" "${RATTLER_CHANNELS[@]}")

sccache --zero-stats

rapids-logger "Building pylibcudf"

# --no-build-id allows for caching with `sccache`
# more info is available at
# https://rattler.build/latest/tips_and_tricks/#using-sccache-or-ccache-with-rattler-build
rapids-telemetry-record build-pylibcudf.log \
  rattler-build build --recipe conda/recipes/pylibcudf \
                    --experimental \
                    --no-build-id \
                    --channel-priority disabled \
                    --output-dir "$RAPIDS_CONDA_BLD_OUTPUT_DIR" \
                    "${RATTLER_CHANNELS[@]}"

rapids-telemetry-record sccache-stats-pylibcudf.txt sccache --show-adv-stats
sccache --zero-stats

rapids-logger "Building cudf"

rapids-telemetry-record build-cudf.log \
   rattler-build build --recipe conda/recipes/cudf \
                    --experimental \
                    --no-build-id \
                    --channel-priority disabled \
                    --output-dir "$RAPIDS_CONDA_BLD_OUTPUT_DIR" \
                    "${RATTLER_CHANNELS[@]}"

rapids-telemetry-record sccache-stats-cudf.txt sccache --show-adv-stats
sccache --zero-stats

rapids-logger "Building dask-cudf"

rapids-telemetry-record build-dask-cudf.log \
    rattler-build build --recipe conda/recipes/dask-cudf \
                    --experimental \
                    --no-build-id \
                    --channel-priority disabled \
                    --output-dir "$RAPIDS_CONDA_BLD_OUTPUT_DIR" \
                    "${RATTLER_CHANNELS[@]}"

rapids-telemetry-record sccache-stats-dask-cudf.txt sccache --show-adv-stats
sccache --zero-stats

rapids-logger "Building cudf_kafka"

rapids-telemetry-record build-cudf_kafka.log \
    rattler-build build --recipe conda/recipes/cudf_kafka \
                    --experimental \
                    --no-build-id \
                    --channel-priority disabled \
                    --output-dir "$RAPIDS_CONDA_BLD_OUTPUT_DIR" \
                    "${RATTLER_CHANNELS[@]}"

rapids-telemetry-record sccache-stats-cudf_kafka.txt sccache --show-adv-stats
sccache --zero-stats

rapids-logger "Building custreamz"

rapids-telemetry-record build-custreamz.log \
    rattler-build build --recipe conda/recipes/custreamz \
                    --experimental \
                    --no-build-id \
                    --channel-priority disabled \
                    --output-dir "$RAPIDS_CONDA_BLD_OUTPUT_DIR" \
                    "${RATTLER_CHANNELS[@]}"

rapids-telemetry-record sccache-stats-custreamz.txt sccache --show-adv-stats
sccache --zero-stats

rapids-logger "Building cudf-polars"

rapids-telemetry-record build-cudf-polars.log \
    rattler-build build --recipe conda/recipes/cudf-polars \
                    --experimental \
                    --no-build-id \
                    --channel-priority disabled \
                    --output-dir "$RAPIDS_CONDA_BLD_OUTPUT_DIR" \
                    "${RATTLER_CHANNELS[@]}"

rapids-telemetry-record sccache-stats-cudf-polars.txt sccache --show-adv-stats

# remove build_cache directory
rm -rf "$RAPIDS_CONDA_BLD_OUTPUT_DIR"/build_cache

rapids-upload-conda-to-s3 python
