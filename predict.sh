python -m nanoT5.main \
    task=ft \
    model.name=google/t5-v1_1-small \
    model.random_init=false \
    predict_only=true \
    model.checkpoint_path="/content/drive/MyDrive/nanoT5/logs/2024-01-17/19-41-33-/best_state_dict.pt" \
    