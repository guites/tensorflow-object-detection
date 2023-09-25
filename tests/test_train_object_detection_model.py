from train_object_detection_model import get_checkpoint_path

class TestGetCheckpointPath:
    def test_loads_from_base_model_when_continue_training_is_true_and_output_model_doesnt_exists():
        ...

    def test_loads_from_output_model_when_continue_training_is_true_and_output_model_exists():
        ...
    
    def test_always_loads_latest_checkpoint_from_output_model_when_continue_training_is_true():
        ...
    
    def test_exits_with_error_when_continue_training_is_true_and_output_model_doesnt_exists_and_base_model_has_no_check_point_file():
        ...
    
    def test_exits_with_error_when_continue_training_is_false_and_output_model_already_exists():
        ...
    
    def test_exits_with_error_when_given_base_model_check_point_file_is_not_found():
        ...
    
    def test_exits_with_error_when_continue_training_is_false_and_base_model_has_no_check_point_file():
        ...
    
