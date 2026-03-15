# shell_exec

Execute Shell commands/scripts from Python (based on `subprocess.run`).

## Usage

```py
import shell_exec

shell_exec("echo 'Hello World'")
# <ExecResult exitcode=0 error='' output='Hello World'>
```

⚠ Use `shlex.quote` to prevent attacks by injections.
```py
import shell_exec
from shlex import quote

msg = "Hello 'World'"
shell_exec(f"echo {msg}")
```

## Possible improvments

- Add Python typehints
- Compute .output / .error on demand.
