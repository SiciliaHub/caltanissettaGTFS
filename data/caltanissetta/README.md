# Script creazione file base

Tutti

```bash
for i in agency stops routes trips stop_times calendar calendar_dates fare_attributes fare_rules shapes frequencies transfers feed_info; do touch $i.txt; done
```

Obbligatori

```bash
for i in agency stops routes trips stop_times calendar; do touch $i.txt; done
```

# Copia dei txt in CSV

```bash
for file in *.txt; do mv "$file" "`basename "$file" .txt`.csv"; done
```
