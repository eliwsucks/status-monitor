from providers import cloudflare, zoho

def run_all():
    print("Checking providers...\n")
    cloudflare.check()
    zoho.check()
    print("\nDone.")

if __name__ == "__main__":
    run_all()
