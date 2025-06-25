import os

def search_files(directory, target_name):
    matches = []
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            if target_name.lower() in name.lower():
                full_path = os.path.join(root, name)
                matches.append(full_path)
    return matches

def main():
    print("🔍 File Search Tool")
    directory = input("Enter the directory to search in (e.g., C:/Users/YourName): ")
    if not os.path.isdir(directory):
        print("❌ Invalid directory path.")
        return
    
    target = input("Enter the file or folder name to search for: ")
    results = search_files(directory, target)
    
    if results:
        print(f"\n✅ Found {len(results)} result(s):")
        for path in results:
            print(f" - {path}")
    else:
        print("❌ No matching files or folders found.")

if __name__ == "__main__":
    main()
