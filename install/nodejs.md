# Node.jsへのインストール

https://github.com/apache/pulsar-client-node#install-on-linux

### Install on mac
Install the Pulsar C++ client on mac.
```
brew install libpulsar
```
Get the installation path of libpulsar
```
brew info libpulsar
Set the variable PULSAR_CPP_DIR with the pulsar-client-cpp path in a mac command tool.
# for example
## Intel x86_64
export PULSAR_CPP_DIR=/usr/local/Cellar/libpulsar/2.9.1_1

## Apple Silicon and Homebrew since 3.0.0
## cf. https://brew.sh/2021/02/05/homebrew-3.0.0/
export PULSAR_CPP_DIR=/opt/homebrew/Cellar/libpulsar/2.9.1_1
```

インクルードファイルへのパスを通す方法は解説されているが、ライブラリーファイルへのパスを通す方法が解説されていない。

そのため、このままでは以下のエラーになる。他にも色々ワーニング等表示されるので、紛らわしいが、この箇所が問題。
```
npm ERR! ld: library not found for -lpulsar
npm ERR! clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

上記同様、`LIBRARY_PATH`へもパスを通す（`lib`サブフォルダーを指定すること）。

```
export LIBRARY_PATH=/opt/homebrew/Cellar/libpulsar/2.10.1_1/lib 
```

インストール成功。

```
yoshiyuki.kono@ykono-rmbp16 node-pulsar % npm install pulsar-client                                      

added 106 packages, and audited 107 packages in 10s

5 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
yoshiyuki.kono@ykono-rmbp16 node-pulsar % ls -l
total 160
drwxr-xr-x@ 105 yoshiyuki.kono  staff   3360 Oct 14 10:54 node_modules
-rw-r--r--    1 yoshiyuki.kono  staff  74488 Oct 14 10:54 package-lock.json
-rw-r--r--    1 yoshiyuki.kono  staff    257 Oct 14 10:54 package.json
yoshiyuki.kono@ykono-rmbp16 node-pulsar % ls node_modules
@gar			delegates		infer-owner		node-addon-api		socks
@mapbox			depd			inflight		node-fetch		socks-proxy-agent
@npmcli			detect-libc		inherits		node-gyp		ssri
@tootallnate		emoji-regex		ip			nopt			string-width
abbrev			encoding		is-fullwidth-code-point	npmlog			string_decoder
agent-base		env-paths		is-lambda		object-assign		strip-ansi
agentkeepalive		err-code		isexe			once			tar
aggregate-error		file-uri-to-path	lru-cache		p-map			tr46
ansi-regex		fs-minipass		make-dir		path-is-absolute	unique-filename
aproba			fs.realpath		make-fetch-happen	promise-inflight	unique-slug
are-we-there-yet	gauge			minimatch		promise-retry		util-deprecate
balanced-match		glob			minipass		pulsar-client		webidl-conversions
bindings		graceful-fs		minipass-collect	readable-stream		whatwg-url
brace-expansion		has-unicode		minipass-fetch		retry			which
cacache			http-cache-semantics	minipass-flush		rimraf			wide-align
chownr			http-proxy-agent	minipass-pipeline	safe-buffer		wrappy
clean-stack		https-proxy-agent	minipass-sized		safer-buffer		yallist
color-support		humanize-ms		minizlib		semver
concat-map		iconv-lite		mkdirp			set-blocking
console-control-strings	imurmurhash		ms			signal-exit
debug			indent-string		negotiator		smart-buffer
yoshiyuki.kono@ykono-rmbp16 node-pulsar % npm install -g pulsar-client

added 106 packages, and audited 107 packages in 9s

5 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
yoshiyuki.kono@ykono-rmbp16 node-pulsar % 

```
