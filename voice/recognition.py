from speechbrain.inference.speaker import SpeakerRecognition

verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec"
)

def is_same_person(audio1, audio2):
    score, prediction = verification.verify_files(audio1, audio2)
    return bool(prediction), float(score)