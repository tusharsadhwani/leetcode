# leetcode

My set of leetcode solutions, written in mypy (statically type-checked Python)

They're all checked by mypy strict-mode, so you can be sure that all types are
correct.

## Testing

Every solution is locally tested using a tool I made: [python-leetcode-runner][1]

To run the tests for yourself, install the tool and run:

```bash
pyleet <name of file>
```

to test all files:

```bash
ls | grep '\.py' | xargs -n1
pyleet
```

## Type checking

You need [mypy](https://github.com/python/mypy) installed.

```bash
mypy --strict .
```

[1]: https://github.com/tusharsadhwani/python-leetcode-runner
