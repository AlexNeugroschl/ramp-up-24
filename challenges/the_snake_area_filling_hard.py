def snakefill(n):
    times_ate = 0
    snake_size = 1
    screensize = n * n
    while snake_size <= screensize:
        snake_size *= 2
        if snake_size <= screensize:
            times_ate += 1
    return times_ate
