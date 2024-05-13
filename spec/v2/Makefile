DIAGRAMS := $(patsubst %.mmd,%.svg,$(wildcard diagrams/*.mmd))
OUTDIR := ../upload/v2
MMDC := mmdc

all: index.html

clean:
	rm -f docs/index.html docs/diagrams/*.svg index.html $(DIAGRAMS)
	rm -rf node_modules/

publish: index.html
	mkdir -p $(OUTDIR)/diagrams
	cp $(DIAGRAMS) $(OUTDIR)/diagrams/
	cp $< $(OUTDIR)

index.html: index.bs $(DIAGRAMS)
	bikeshed --md-status=iso/PAS spec $< $@

%.svg: %.mmd $(MMDC)
	$(MMDC) -i $< -o $@

serve: $(DIAGRAMS)
	bikeshed serve index.bs

$(MMDC):
	npm install -g @mermaid-js/mermaid-cli

.PHONY: publish clean serve
