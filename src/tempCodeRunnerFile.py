env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path)
API_KEY = os.getenv("SECRET_KEY")
if not API_KEY:
    raise ValueError("SECRET_KEY is not set")
print(API_KEY)