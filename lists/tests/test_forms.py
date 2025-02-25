from django.test import TestCase

from lists.forms import ItemForm, EMPTY_ITEM_ERROR


class ItemFormTest(TestCase):

    # def test_form_renders_item_text_input(self):
    #     form = ItemForm()
    #     self.fail(form.as_p())

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )
