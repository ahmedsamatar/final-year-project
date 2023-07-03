<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you</h1>

                <p>Your booking will be processed within 48 hours. You will recieve an email shortly for the confirmation of
                    the booking.</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Success | Footy4U' // shows user which page currently on via the tab on browser
    },
}
</script>