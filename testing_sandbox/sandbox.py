import subprocess

def simulate_patch_test(patch_code):
    # Deploy patch in a sandbox environment
    result = subprocess.run(
        ["./sandbox_env.sh", patch_code],
        capture_output=True,
        text=True
    )
    return result.stdout
