
import subprocess

def error_calculate(count):    

    file_path = f'validation-tests/{count}.txt'
    total_images = 474

    # Command for positive and non-child errors
    e1_command = f'findstr /C:"Positive" "{file_path}" | findstr /C:"non-child"'        
    e1_result = subprocess.run(e1_command, shell=True, text=True, capture_output=True)
    if e1_result.returncode == 0:
        e1 = len(e1_result.stdout.splitlines())
        print(f"Number of matching lines: {e1}")
    else:
        print("No matching strings found.")
        e1 = 0
    

    # Command for negative and child errors
    e2_command = f'findstr /C:"Negative" "{file_path}" | findstr /C:": child"'

    e2_result = subprocess.run(e2_command, shell=True, text=True, capture_output=True)
    if e2_result.returncode == 0:
        e2 = len(e2_result.stdout.splitlines())
        print(f"Number of matching lines: {e2}")
    else:
        print("No matching strings found.")
        e2 = 0
    
    # Calculate errors and successes
    total_errors = e1 + e2
    total_success = total_images - total_errors
    success_percent = (total_success * 100) / total_images
    error_percent = (total_errors * 100) / total_images

    # Append results to file
    with open('tests-results.txt', 'a') as result_file:
        result_file.write(f"{count}\t{total_success}\t{success_percent:.2f}%\t{total_errors}\t{error_percent:.2f}%\n")

    # Return total success and errors
    return [total_success, total_errors]

