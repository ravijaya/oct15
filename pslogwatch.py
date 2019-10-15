def log_watch(log_file):
    """generator """
    try:
        with open(log_file) as fp:  # context manager
            fp.seek(0, 2)

            while True:
                content = fp.read()

                if content:
                    yield content

    except (FileNotFoundError, IOError) as error:
        print(error)


for temp in log_watch('messages'):
    print(temp)

