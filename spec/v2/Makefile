DIAGRAMS := $(patsubst %.mmd,%.svg,$(wildcard diagrams/*.mmd))
OUTDIR := ../../upload/v2
MMDC := mmdc
STATUS ?= ""

all: index.html

clean:
	rm -f docs/index.html docs/diagrams/*.svg index.html $(DIAGRAMS)
	rm -rf node_modules/

publish: index.html computed-metadata.include
	mkdir -p $(OUTDIR)/diagrams
	cp $(DIAGRAMS) $(OUTDIR)/diagrams/
	cp $^ $(OUTDIR)

index.html: index.bs $(DIAGRAMS)
	bikeshed spec $< $@ --md-text-macro="$(STATUS)"

%.svg: %.mmd $(MMDC)
	$(MMDC) -i $< -o $@

serve: $(DIAGRAMS)
	bikeshed serve index.bs

$(MMDC):
	npm install -g @mermaid-js/mermaid-cli

pull-metadata:
	curl -o computed-metadata.include https://raw.githubusercontent.com/wbcsd/tr/main/data-exchange-protocol/computed-metadata.include

.PHONY: publish clean serve pull-metadata
