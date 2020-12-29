# cURL Option Summary
Long  |  Short  | Arg | Notes
:----------------|:-----|:----:|------------------------------------------------------------
`--request`  | `-X`           | Yes       | GET, POST, PUT, DELETE
`--url`      |                | No | Specify URL for target of HTTP request; can also omit this option and specify as *last* on command line, after all options.
`--trace` ||Yes| Give file that shows trace information flow.
`--verbose`| `-v` | No | Verbose output; can be used to see request headers
`--header` | `-H` | Yes | Specify string to be used as a header line
`--head` | `-I` | No | Send `HEAD` as HTTP method, to get just headers as return
`--get` | `-G` | No | Select `GET` as HTTP method
`--include` | `-I` | No | Show response headers as well as body as output
`--data` | `-d` | Yes | Argument can be `'key=value` for specifying one Form for POST body, or can be `'<json string>'` to specify entire body; makes request a POST
`--silent` |`-s`|No| Hide progress meter
