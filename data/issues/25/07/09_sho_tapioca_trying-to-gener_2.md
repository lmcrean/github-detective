issue title: Trying to generate DSLs with add-on for a non-processable constant errors
labels: bug
comment count: 1
hyperlink: https://github.com/shopify/tapioca/issues/2348
status: open
date opened: 2025-07-09
repo 30d_merge_rate: 12

====

description:
When saving a file that contains a constant that cannot be processed by any DSL compilers, the add-on errors. The error is rescued and nothing actually happens, but it prints to the output tab and looks like something crashed.

It would be nice to just return early without printing any errors.

```
~/tapioca/lib/tapioca/dsl/pipeline.rb:63:in 'Tapioca::Dsl::Pipeline#run': Tapioca::Error
  from ~/tapioca/lib/tapioca/commands/abstract_dsl.rb:64:in 'Tapioca::Commands::AbstractDsl#generate_dsl_rbi_files'
  from ~/tapioca/lib/tapioca/commands/dsl_generate.rb:17:in 'Tapioca::Commands::DslGenerate#execute'
  from ~/tapioca/lib/tapioca/commands/command.rb:25:in 'block in Tapioca::Commands::Command#run'
```

===

comment #1 by KaanOzkan, 2025-07-09, 21:06:02
I think this is a side effect of the migration in https://github.com/Shopify/tapioca/pull/2322. Previously we were raising a Thor::Error and it was being rescued by Thor. Now it's a Tapioca::Error, being rescued by the rails add-on and outputted.
