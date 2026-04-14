import gradio as gr

# --- LAYER 1: THE MANUAL ALGORITHM (Algorithm Implementation Rubric) ---
def quick_sort(playlist, steps):
    """
    Manual Quick Sort implementation to rank songs by duration.
    This avoids built-in functions like .sort() or sorted().
    'steps' records the process for the visual simulation.
    """
    if len(playlist) <= 1:
        return playlist
    
    # Abstraction: Choosing the middle element as the pivot
    pivot_index = len(playlist) // 2
    pivot = playlist[pivot_index]
    pivot_duration = pivot['duration']
    
    steps.append(f"LOG: Picking pivot '{pivot['title']}' with length {pivot_duration}s")
    
    # Decomposition: Splitting the list into three parts
    left = [x for x in playlist if x['duration'] < pivot_duration]
    middle = [x for x in playlist if x['duration'] == pivot_duration]
    right = [x for x in playlist if x['duration'] > pivot_duration]
    
    steps.append(f"LOG: Partitioned into {len(left)} shorter and {len(right)} longer tracks.")
    
    # Pattern Recognition: Recursive calls to repeat the process
    return quick_sort(left, steps) + middle + quick_sort(right, steps)

# --- LAYER 2: DATA PROCESSING (Solving the Problem Rubric) ---
def start_sorting(raw_text):
    """
    Handles input validation and triggers the sorting simulation.
    """
    if not raw_text.strip():
        return "Please enter some song data.", "Waiting for input..."

    try:
        songs = []
        lines = raw_text.strip().split("\n")
        
        for line in lines:
            if "," not in line:
                return "Error: Use 'Title, Seconds' format (e.g., Starboy, 230)", ""
            
            parts = line.split(",")
            title = parts[0].strip()
            # Input Validation: Ensuring duration is a number
            duration = float(parts[1].strip()) 
            songs.append({"title": title, "duration": duration})
        
        simulation_log = ["--- Starting Simulation ---"]
        sorted_playlist = quick_sort(songs, simulation_log)
        
        # Formatting the final result for the UI
        result = "Sorted Playlist (Shortest to Longest):\n"
        for i, s in enumerate(sorted_playlist):
            result += f"{i+1}. {s['title']} — {s['duration']}s\n"
            
        return result, "\n".join(simulation_log)

    except ValueError:
        return "Error: Duration must be a valid number. Check your entry.", ""
    except Exception as e:
        return f"An unexpected error occurred: {e}", ""

# --- LAYER 3: THE GRADIO GUI (UI Rubric) ---
with gr.Blocks(title="Playlist Vibe Builder") as demo:
    gr.Markdown("# Playlist Vibe Builder")
    gr.Markdown("Organize your tracks by length using a manual **Quick Sort** algorithm.")
    
    with gr.Row():
        with gr.Column():
            song_input = gr.Textbox(
                label="Input Songs", 
                placeholder="Example:\nTrack A, 180\nTrack B, 120\nTrack C, 240",
                lines=8
            )
            sort_btn = gr.Button("Build Sorted Playlist", variant="primary")
        
        with gr.Column():
            output_list = gr.Textbox(label="Result", lines=5)
            output_log = gr.Textbox(label="Algorithm Simulation Log", lines=8)

    sort_btn.click(
        fn=start_sorting, 
        inputs=song_input, 
        outputs=[output_list, output_log]
    )
    
    gr.Markdown("### Instructions\n1. Enter one song per line: `Name, Duration`.\n2. Click the button to see the Quick Sort partitioning steps.")

if __name__ == "__main__":
    demo.launch()
