def optimal_page_replacement(pages, capacity):
    page_faults = 0
    page_frames = [-1] * capacity
    next_use = [-1] * capacity

    for i, page in enumerate(pages):
        if page not in page_frames:
            page_faults += 1

            if -1 in page_frames:
                # If there is an empty slot, insert the page
                empty_slot = page_frames.index(-1)
                page_frames[empty_slot] = page
                next_use[empty_slot] = find_next_use(pages, i)
            else:
                # Find the page in page_frames with the farthest next use
                idx = next_use.index(max(next_use))
                page_frames[idx] = page
                next_use[idx] = find_next_use(pages, i)

    print("Page Faults:", page_faults)

def find_next_use(pages, current_index):
    for i in range(current_index + 1, len(pages)):
        if pages[i] in pages[current_index + 1:]:
            return i
    return float('inf')  # If the page is not used anymore, set next use to infinity

if __name__ == "__main__":
    # Example pages reference string
    pages_reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    
    # Set the number of page frames (capacity)
    page_frame_capacity = 3
    
    optimal_page_replacement(pages_reference, page_frame_capacity)
