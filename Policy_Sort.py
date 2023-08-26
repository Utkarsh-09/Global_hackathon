def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['Policy-Number'] <= right_half[j]['Policy-Number']:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    policy_data = [
        # List of dictionaries representing each record
        # Example: {'Policy-Number': 'ABC123', 'Policy-Holder-Name': 'John Doe', ...}
        # Insert your policy data here
    ]

    print("Sorting policy data using Merge Sort...")
    merge_sort(policy_data)
    print("Policy data sorted.")
    # At this point, the 'policy_data' list is sorted based on 'Policy-Number'

if __name__ == "__main__":
    main()
