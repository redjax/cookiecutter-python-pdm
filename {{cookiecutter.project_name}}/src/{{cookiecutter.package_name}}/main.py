import logging

log = logging.getLogger(__name__)

def main():
    log.info("{{ cookiecutter.package_name }}.main.main() called.")
    pass

if __name__ == "__main__":
    log.info("Initialized cookiecutter project: {{ cookiecutter.package_name }}.")
    
    main()