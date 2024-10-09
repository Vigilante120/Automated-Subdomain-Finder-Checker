import subprocess

def main():
    url = input("Please enter the URL ([+]Format = google.com): ")

    subfinder_command = f"subfinder -d {url} > subdomains.txt"
    print("Running subfinder...")
    subprocess.run(subfinder_command, shell=True)

    threads = input("Please enter the number of threads: ")

    httpx_command = f"cat subdomains.txt | httpx-toolkit -ports 80,443,8080,8000,8888 -threads {threads} > subdomains_alive.txt"
    print("Running httpx-toolkit...")
    subprocess.run(httpx_command, shell=True)

    print("Process completed. Check 'subdomains_alive.txt' for results.")

if __name__ == "__main__":
    main()
