def validate_patch(test_results):
    success_threshold = 0.9  # Example success threshold
    success_rate = test_results.get("success_rate", 0)
    return success_rate >= success_threshold
