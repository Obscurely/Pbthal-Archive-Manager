import os
import re


def search(query: str):
    query = re.sub(r"[^a-zA-Z0-9 ]", "", query).lower().strip()

    # Move on to searching part
    archives = {}

    recordings = 0

    for file in os.listdir("data/archives"):
        lines = open("data/archives/" + file).readlines()
        parsed_lines = []
        for line in lines:
            parsed_lines.append(line.replace("\n", ""))
        recordings += len(lines)
        archives[file] = parsed_lines

    archives_links = {}

    for line in open("data/archives_links").readlines():
        line_split = line.split(" ")
        archives_links[line_split[0]] = line_split[1].replace("\n", "")

    print(f"Successfully loaded {recordings} recordings\n")

    print(f"Searching for: {query}\n")

    query_words = query.split(" ")

    final_results = {}

    for archive in archives:
        results = []
        for recording in archives[archive]:
            is_match = False
            current_recording = str(recording).lower()
            for word in query_words:
                if len(current_recording.split(word)) >= 2:
                    is_match = True
                else:
                    is_match = False
                    break
            if is_match:
                results.append(recording)
        if len(results) > 0:
            final_results[archive] = results

    if len(final_results) == 0:
        print("There were no results for your search query, try readjusting it maybe.")
    else:
        for result in final_results:
            print(f"In {result} (archive link: {archives_links[result]})")
            print("Literal matches:")
            for match in final_results[result]:
                print(f"\t- {match}")
            print()
            print("Download link matches:")
            for link in open(f"data/recordings_links/{result}"):
                is_match = False
                current_link = link.lower()
                for word in query_words:
                    if len(current_link.split(word)) >= 2:
                        is_match = True
                    else:
                        is_match = False
                        break
                if is_match:
                    print(f"\t- {link}")

            print("\n")
        print("The archive password is always: b0nn13mCmurr@y")
