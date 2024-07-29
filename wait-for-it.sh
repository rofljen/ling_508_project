#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available
# source: https://github.com/vishnubob/wait-for-it

TIMEOUT=15
QUIET=0
HOST=""
PORT=""
cmd=""

usage() {
    echo "Usage: $0 host:port [-t timeout] [-- command args]"
    echo "  -q | --quiet                          Don't output any status messages"
    echo "  -t TIMEOUT | --timeout=timeout        Timeout in seconds, zero for no timeout"
    echo "  -- COMMAND ARGS                       Execute command with args after the test finishes"
    exit 1
}

wait_for() {
    if [[ "$TIMEOUT" -gt 0 ]]; then
        echo "Waiting $TIMEOUT seconds for $HOST:$PORT"
    else
        echo "Waiting for $HOST:$PORT without a timeout"
    fi

    start_ts=$(date +%s)
    while :
    do
        if [[ "$QUIET" -eq 0 ]]; then
            echo "Checking $HOST:$PORT..."
        fi
        nc -z "$HOST" "$PORT"
        result=$?
        if [[ $result -eq 0 ]]; then
            end_ts=$(date +%s)
            echo "$HOST:$PORT is available after $((end_ts - start_ts)) seconds"
            break
        fi
        sleep 1
    done
}

wait_for_wrapper() {
    if [[ "$cmd" != "" ]]; then
        if [[ "$result" -ne 0 ]]; then
            echo "Timeout occurred after waiting $TIMEOUT seconds for $HOST:$PORT"
        fi
        exec $cmd
    else
        exit $result
    fi
}

while [[ $# -gt 0 ]]
do
    case "$1" in
        *:* )
        HOST=$(echo $1 | cut -d : -f 1)
        PORT=$(echo $1 | cut -d : -f 2)
        shift 1
        ;;
        -q | --quiet)
        QUIET=1
        shift 1
        ;;
        -t)
        TIMEOUT=$2
        shift 2
        ;;
        --timeout=*)
        TIMEOUT="${1#*=}"
        shift 1
        ;;
        --)
        shift
        cmd="$@"
        break
        ;;
        *)
        usage
        ;;
    esac
done

if [[ "$HOST" = "" || "$PORT" = "" ]]; then
    echo "Error: you need to provide a host and port to test."
    usage
fi

wait_for
wait_for_wrapper
