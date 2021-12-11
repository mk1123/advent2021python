day = $(shell date +'%-d')

new:
	@echo "Creating new file for day" $(day)"..."

	@if [ $(day) -lt 10 ] ; then \
  		cp template 0$(day).py; \
		git add 0$(day).py; \
  	else \
		cp template $(day).py; \
		git add $(day).py; \
    fi
	@echo "Files successfully created.. happy hacking :)"
	@echo "INFO: puzzle input still needs to be fetched"