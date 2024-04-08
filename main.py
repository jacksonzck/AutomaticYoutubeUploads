from googleapiclient.discovery import build
import dotenv
config = dotenv.dotenv_values(".env")

def main():
    with build('youtube', 'v3', developerKey = config["KEY"]) as service:
        print(service.videos)
        pass

if __name__ == "__main__":
    main()