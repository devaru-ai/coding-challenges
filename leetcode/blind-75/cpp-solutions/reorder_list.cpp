class Solution {
public:
  void reorderList(ListNode* head) {
    if (!head || !head->next || !head->next->next) return;
    ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next) {
      slow = slow->next;
      fast = fast->next->next;
    }
    ListNode* prev = nullptr;
    ListNode* curr = slow->next;
    while(curr) {
      ListNode* nextNode = curr->next;
      curr->next = prev;
      prev = curr;
      curr = nextNode;
    }
    slow->next = nullptr; // break the list
    ListNode* first = head;
    ListNode* second = prev;
    while(second) {
      ListNode* tmp1 = first->next;
      ListNode* tmp2 = second->next;

      first->next = second;
      second->next = tmp1;

      first = tmp1;
      second = tmp2;
    }
  }
};
