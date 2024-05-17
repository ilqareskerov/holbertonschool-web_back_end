-- This is a line of text
CREATE TRIGGER decrease_items AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
