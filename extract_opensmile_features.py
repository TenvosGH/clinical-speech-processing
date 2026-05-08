import os
import pandas as pd
import opensmile


def extract_opensmile_features(audio_dir, output_file, feature_set, feature_level):
    smile = opensmile.Smile(
      feature_set=feature_set,
      feature_level=feature_level,
    )

    all_features = []
    for root, dirs, files in os.walk(audio_dir):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                features = smile.process_file(file_path)
                features['file'] = file
                speaker_id = root.split('\\')[-2]
                features['participant_id'] = speaker_id
                all_features.append(features)

    combined_features = pd.concat(all_features, ignore_index=True)
    combined_features.to_csv(output_file, index=False)
    return combined_features


if __name__ == '__main__':
    # extract_opensmile_features(input_path, output_file, opensmile.FeatureSet.ComParE_2016, feature_level=opensmile.FeatureLevel.Functionals)
    # extract_opensmile_features(input_path, output_file, opensmile.FeatureSet.eGeMAPSv02, feature_level=opensmile.FeatureLevel.LowLevelDescriptors)
    input_path = 'sustained_vowels_segmented'
    output_file = 'opensmile_features_df.csv'
    extract_opensmile_features(input_path, output_file, opensmile.FeatureSet.ComParE_2016,
                               feature_level=opensmile.FeatureLevel.Functionals)