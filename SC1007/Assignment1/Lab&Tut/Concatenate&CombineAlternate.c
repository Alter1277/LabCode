int concatenate(ListNode **ptrHead1, ListNode *head2){
	/*ListNode *temp = *ptrHead1;
	// Both lists empty, let's return a -1 error value
	if (*ptrHead1 == NULL && head2 == NULL)
		return -1;
	// Empty first list, just set the head pointer of list 1 to point to first node of list 2
	if (temp == NULL){
		*ptrHead1 = head2;
		return 0;
	}
	// Empty second list, nothing to do
	if (head2 == NULL)
		return 0;
	// Traverse the first list to get to the last node
	// Notice we check for the value of the next pointer for the current node
	while (temp->next != NULL)
		temp = temp->next;
	temp->next = head2;
	return 0;*/
	ListNode *temp;
	if(*ptrHead1 == NULL && head2 == NULL) return -1;
	if(*ptrHead1 == NULL) {
		*ptrHead1 = head2;
		return 0;}
	if(head2 == NULL) return 0;
	temp = *ptrHead1;
	while(temp->next != NULL) temp = temp->next;
	temp->next = head2;
	return 0;
	
}
int combineAlternating(ListNode **ptrHead, ListNode *head1, ListNode *head2)
{
	ListNode *temp;
	if (head1 == NULL && head2 == NULL) return -1;
	// If both remaining lists are empty, we're done
	// We know that at least one of the lists has a remaining node inside this while loop
	// Check in pairs each cycle: List #1, then List #2
	while (head1 != NULL || head2 != NULL){// Adding the first node, remember to update the head pointer
		if (*ptrHead == NULL){
			if (head1 != NULL){
				*ptrHead = malloc(sizeof(ListNode));
				(*ptrHead)->num = head1->num;
				head1 = head1->next;
				temp = *ptrHead;
				if (head2 != NULL){
					temp->next = malloc(sizeof(ListNode));
					temp->next->num = head2->num;
					temp = temp->next;
					head2 = head2->next;
				}
			}
			else{
				*ptrHead = malloc(sizeof(ListNode));
				(*ptrHead)->num = head2->num;
				head2 = head2->next;
				temp = *ptrHead;
			}
		}
		else{
			if (head1 != NULL){
				temp->next = malloc(sizeof(ListNode));
				temp->next->num = head1->num;
				temp = temp->next;
				head1 = head1->next;
			}
		if (head2 != NULL){
			temp->next = malloc(sizeof(ListNode));
			temp->next->num = head2->num;
			temp = temp->next;
			head2 = head2->next;
			}
		}
	}
	temp->next =NULL;
	return 0;
}
