# Clinical Speech Processing
## Overview

The goal of this repository is to provide code and utilities for audio preprocessing and acoustic analysis in clinical speech research.

The workflow was developed for a clinical study investigating the use of voice technology to identify opioid use in patients receiving treatment for opioid use disorder. Speech tasks in the study included:

- Reading the participant’s ID and the current time
- Reading a fixed passage (e.g., Rainbow Passage)
- Sustaining vowels for 5 seconds
- Answering open-ended clinical questions

To simplify the recording workflow and reduce interruptions during data collection, the entire session was recorded as a single continuous audio file rather than requiring separate recordings for each task.

This repository contains automated processing scripts that help segment, align, and analyze long-form clinical audio recordings.

## Included Processing Steps

### 1. Automatic Transcription

Long audio recordings are automatically transcribed to help identify task boundaries and approximate timestamps for segmentation.

Script:
```bash
run_transcription.py
```

This script recursively searches for `.wav` files in the dataset directory and uses the Whisper large speech recognition model to generate automatic transcriptions. The transcription for each audio file is saved as a corresponding `.lab` file with the same filename.

The generated transcription files can be used for downstream segmentation and alignment tasks, including Montreal Forced Aligner (MFA) processing and locating specific speech tasks within long-form recordings.

### 2. Forced Alignment

The repository includes scripts for running the Montreal Forced Aligner (MFA), a widely used speech-text alignment tool. Forced alignment was primarily used to support vowel-level acoustic analysis.

Script:
```bash
run_mfa.py
```

This script runs Montreal Forced Aligner (MFA) on sustained vowel recordings using the `english_us_arpa` acoustic and pronunciation models. The alignment process generates timestamped phoneme-level annotations that can be used for downstream acoustic measurements and segment-level analysis.

The script is configured to process all files within the input directory and save aligned outputs to a separate output directory. Alignment parameters such as beam width, overwrite behavior, and cleanup options are included to support batch processing workflows.

### 3. Acoustic Feature Extraction

Acoustic features can be extracted using OpenSMILE for downstream speech and biomarker analysis.

Script:
```bash
extract_opensmile_features.py
```

This script extracts acoustic features from `.wav` audio files using the OpenSMILE toolkit. The current configuration uses the ComParE 2016 feature set with functional-level features, though other feature sets and feature levels supported by OpenSMILE can also be configured.

The script recursively processes audio files within the input directory, extracts acoustic features for each recording, and combines the results into a single CSV file for downstream statistical analysis and machine learning workflows. File names and participant IDs are also stored alongside the extracted features to support dataset organization and analysis.
