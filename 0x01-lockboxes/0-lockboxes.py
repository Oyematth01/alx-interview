#!/usr/bin/python3
def canUnlockAll(boxes):
	"""
	Determines if all boxes can be unlocked.
	
	Args:
	boxes (list of lists): Each list contains keys for other boxes.
	
	Var:
	total_boxes: Stores the total number of boxes we need to check.
	unlocked_boxes is a list that tracks whether each box is unlocked.
	
	Returns:
	boolean: True if all boxes can be unlocked, False otherwise.
	"""
	# Total number of boxes
	total_boxes = len(boxes)

	# Create a list to track which boxes are unlocked
	unlocked_boxes = [False] * total_boxes

	# The first box (index 0) is always unlocked
	unlocked_boxes[0] = True

	# List of keys we have collected, starting with keys from box 0
	keys = [0]

	while keys:
			current_key = keys.pop(0)
			for new_key in boxes[current_key]:
					#To ensure the key is valid, it must be within the range of available boxes
					if new_key < total_boxes:
							# If the box hasn't already been unlocked
							if not unlocked_boxes[new_key]:
									# Unlock the box
									unlocked_boxes[new_key] = True
									# Add the new keys found in this box to our list of keys
									keys.append(new_key)

	return all(unlocked_boxes)
