class MainPageLocators:
    SEARCH_INPUT = "[class=header-search__input]"
    SEARCH_BUTTON = "[class=header-search__button]"
    PRODUCT_TITLE_HEAD = "[class=product-title__head]"
    PRODUCT_OLD_PRICE = "[class=product-price__old]"
    PRODUCT_DISCOUNT_PRICE = "[class*=product-price__value--discount]"
    PRODUCT_BUY_BUTTON = "[class*='button action-button']"
    PRODUCT_CHECKOUT_BUTTON = "//*[contains(text(), 'Оформить')]"
    HEADER_CART_BUBBLE = "[class*=header-cart__badge]"
    HEADER_CART_BUTTON = "a[class*=header-cart]"


class CartPageLocators:
    CART_ITEM = "[class=cart-item]"
    CART_PAGE_TITLE = "[class*='cart-page__title']"
    CARD_PRODUCT_OLD_PRICE = "[class=product-price__old]"
    CARD_PRODUCT_DISCOUNT_PRICE = "[class*=product-price__value--discount]"
