# shell_exec

Execute Shell commands/scripts from Python (based on `subprocess.run`).

## Usage

```py
import shell_exec

shell_exec("echo 'Hello World'")
# <ExecResult exitcode=0 error='' output='Hello World'>
```

⚠ You can use f-string to write the command line. However, this is unsafe if used with untrusted/external data.

## Possible improvments

- Add Python typehints
- Compute .output / .input on demand.
- Prevent injections.
